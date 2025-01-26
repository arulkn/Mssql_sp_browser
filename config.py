import os  # Add this import
import json

# Default configuration
DEFAULT_CONFIG = {
    'driver': 'SQL Server',
    'server': 'ARULDESKTOP',
    'database': 'OLTP',
    'trusted_connection': 'yes',
    'username': '',
    'password': ''
}

def load_config():
    try:
        if os.path.exists('db_config.json'):  # This requires the 'os' module
            with open('db_config.json', 'r') as f:
                return json.load(f)
    except Exception:
        pass
    return DEFAULT_CONFIG

def save_config(config):
    with open('db_config.json', 'w') as f:
        json.dump(config, f)