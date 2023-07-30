# URL Shortener

URL Shortener is a simple Flask web application that allows users to shorten long URLs to more manageable, short URLs. The application stores the original URL along with its shortened counterpart in a MongoDB database. When users visit the shortened URL, they are redirected to the original long URL.

## Getting Started

### Prerequisites

Before running the application, make sure you have the following installed:

- Python (3.7 or higher)
- MongoDB (Make sure you have a MongoDB server up and running or use a cloud-based MongoDB service)

### Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/mirolaukka/url-shortener.git
```

2. Change into the project directory:

```
cd url-shortener
```

3. Create a virtual environment (optional but recommended):

```
python -m venv venv
```

4. Activate the virtual environment:

- On Windows:

```
venv\Scripts\activate
```

- On macOS and Linux:

```
source venv/bin/activate
```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

6. Create a `.env` file in the root of the project and add your MongoDB credentials:

```
MONGO_PASSWORD=your_mongodb_password
FLASK_APP=main
FLASK_RUN_PORT=8080
```

Replace `your_mongodb_password` with the password for your MongoDB user.

### Usage

To run the application, execute the following command in the terminal:

```
flask run
```

This will start the Flask development server, and the application will be accessible at `http://127.0.0.1:8080/` in your web browser.

### How to Shorten URLs

1. Open the application in your web browser at `http://127.0.0.1:8080/`.

2. In the input field, enter the long URL you want to shorten.

3. Click the "Shorten URL" button.

4. The application will generate a shortened URL for you, which you can copy and share.

### Redirecting to Original URLs

To visit the original long URL associated with a shortened URL, simply enter the shortened URL in your web browser's address bar, and you will be redirected to the original URL.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- This application uses Flask, a micro web framework for Python.
- The URL shortening algorithm is based on the FNV-1a hash function and Base62 encoding.
