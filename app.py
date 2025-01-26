import os  # Add this import
from flask import Flask
from routes import main_routes
from config import load_config

app = Flask(__name__)
app.secret_key = os.urandom(24)  # This requires the 'os' module

# Load configuration
app.config.update(load_config())

# Register blueprints
app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)