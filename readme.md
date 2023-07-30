# URL Shortener

URL Shortener is a simple Flask web application that allows users to shorten long URLs to more manageable, short URLs. The application stores the original URL along with its shortened counterpart in a MongoDB database. When users visit the shortened URL, they are redirected to the original long URL.

## Features

- Shorten long URLs to shorter ones for easy sharing.
- Redirect users to the original long URL when they visit the shortened URL.
- Utilizes MongoDB to store the original URLs and their corresponding shortened URLs.

## Technologies Used

- Python
- Flask
- MongoDB
- FNV-1a Hash Function
- Base62 Encoding



## How the URL Shortener Works

1. The user provides a long URL to the application.
2. If the long URL is already in the database, the application retrieves the corresponding shortened URL. Otherwise, it generates a new shortened URL.
3. The original URL and its shortened version are stored in the MongoDB database.
4. The user is presented with the shortened URL.
5. When the user visits the shortened URL, the application looks up the original URL in the database and redirects the user to the corresponding long URL.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This application uses Flask, a micro web framework for Python.
- The URL shortening algorithm is based on the FNV-1a hash function and Base62 encoding.
