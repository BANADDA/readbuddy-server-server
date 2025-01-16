from src.server import app

# Export the app variable for Gunicorn
application = app  

if __name__ == '__main__':
    app.run()