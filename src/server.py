from flask import Flask
from flask_cors import CORS

from src.routes.index import init_routes

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Initialize your routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
