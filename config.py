"""
Configuration Module for GreenGuile

Manages system configuration and settings.
"""

import json
import os


class ConfigManager:
    def __init__(self, config_file="config.json"):
        """
        Initialize the configuration manager.
        
        Args:
            config_file (str): Path to the configuration file
        """
        self.config_file = config_file
        self.config = {
            "sound_interval": 300,  # seconds
            "volume": 80,  # percentage
            "active_hours": {
                "start": "06:00",
                "end": "18:00"
            },
            "season": "spring",
            "phone_number": "+1234567890"
        }
        self.load_config()
        
    def load_config(self):
        """Load configuration from file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
                print("Configuration loaded from file")
            except Exception as e:
                print(f"Error loading configuration: {e}")
        else:
            self.save_config()
            print("Default configuration created")
            
    def save_config(self):
        """Save configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            print("Configuration saved to file")
        except Exception as e:
            print(f"Error saving configuration: {e}")
            
    def get(self, key, default=None):
        """
        Get a configuration value.
        
        Args:
            key (str): Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        return self.config.get(key, default)
        
    def set(self, key, value):
        """
        Set a configuration value.
        
        Args:
            key (str): Configuration key
            value: Configuration value
        """
        self.config[key] = value
        self.save_config()