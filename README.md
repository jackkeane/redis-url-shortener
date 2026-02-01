🚀 Redis URL Shortener
A lightning-fast URL shortening service built with Python, Flask, and Redis. This project demonstrates how to use an in-memory data store to handle high-speed redirections and unique ID generation.

🛠️ Tech Stack
Backend: Python 3.x, Flask

Database: Redis

Frontend: HTML5, Bootstrap 5 (CDN)

📂 Project Structure
Plaintext
url-shortener/
├── app.py              # Flask application & Redis logic
├── templates/
│   └── index.html      # UI for the shortener
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
⚙️ Setup & Installation
1. Prerequisites
Ensure you have Redis installed and running.

macOS: brew install redis then brew services start redis

Linux: sudo apt install redis-server

Docker: docker run -p 6379:6379 -d redis

2. Clone and Install
Bash
# Create project folder
mkdir url-shortener && cd url-shortener

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install flask redis
3. Run the Application
Bash
python app.py
The app will be available at: http://127.0.0.1:5000

💡 How it Works
Unique IDs: The app uses Redis INCR on a global counter (url_id_counter). This ensures every link gets a unique integer ID, even with concurrent users.

Short Codes: The integer ID is converted to a hexadecimal string (e.g., 255 becomes ff) to create a short URL slug.

Storage: The mapping is stored in a Redis Hash named links.

Key: links

Field: short_code

Value: long_url

Redirection: When a user visits /<short_code>, the app performs a HGET lookup. If found, it issues a 302 Redirect.

📝 License
MIT