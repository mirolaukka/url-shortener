import os
import validators
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from flask import Flask, render_template, request, Response, redirect

load_dotenv()

# Set up the MongoDB connection URI
uri = "mongodb+srv://mjlaukka:{password}@url-shortener.9harp9h.mongodb.net/?retryWrites=true&w=majority".format(password=os.getenv("MONGO_PASSWORD"))

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Check if the connection was successful
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Select the database and collection
db = client['url_shortener']
collection = db['short_urls']


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form.get("original_url")
        
        if validators.url(original_url):
            shortened_url = request.url + shorten_url(original_url)
        else:
            shortened_url = "Not a valid url!"
        
        return render_template("index.html", shortened_url=shortened_url)
    return render_template("index.html")

@app.route("/<short_url>")
def redirect_to_original(short_url):
    original_url = collection.find_one({'shortened_url': short_url})
    if original_url:
        return redirect(original_url['original_url'])
    else:
        return "not found", 404

def shorten_url(original_url: str) -> str:
    """
    Shorten the given URL and store it in the database if it doesn't already exist.

    Parameters:
        original_url (str): The original URL to be shortened.

    Returns:
        str: The shortened URL.
    """
    # Check if the URL already exists in the database
    existing_url = collection.find_one({'original_url': original_url})
    if existing_url:
        return existing_url['shortened_url']

    # If not, generate a new shortened URL and store it in the database
    counter = db['counter'].find_one_and_update(
        {'_id': 'url_counter'},
        {'$inc': {'count': 1}},
        return_document=True,
        upsert=True
    )
    short_url = base62_encode(fnv_1a_hash(original_url))
    collection.insert_one({'original_url': original_url, 'shortened_url': short_url})
    return short_url

def base62_encode(num: int) -> str:
    """
    Encode an integer into a Base62 string.

    Parameters:
        num (int): The integer to be encoded.

    Returns:
        str: The Base62-encoded string.
    """
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    base = len(characters)
    encoded_string = ""

    if num == 0:
        return characters[0]

    while num:
        num, remainder = divmod(num, base)
        encoded_string = characters[remainder] + encoded_string

    return encoded_string

def fnv_1a_hash(string: str, seed: int = 0x811c9dc5) -> int:
    """
    Implements the FNV-1a hash function.

    Parameters:
        string (str): The input string to be hashed.
        seed (int): Optional seed value (default is 0x811c9dc5).

    Returns:
        int: The FNV-1a hash value as an unsigned 32-bit integer.
    """
    fnv_prime = 0x01000193  # FNV prime (32-bit)
    hash_val = seed

    for char in string.encode('utf-8'):
        hash_val ^= char
        hash_val *= fnv_prime

    return hash_val & 0xFFFFFFFF  # Ensure the result is a 32-bit integer