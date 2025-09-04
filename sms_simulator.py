"""
SMS Simulator for GreenGuile

Simulates receiving SMS commands for testing purposes.
"""

import time
from green_guile import GreenGuile
from sms_handler import SMSHandler
from config import ConfigManager


def simulate_sms_system():
    """Simulate the full SMS-controlled system."""
    print("Starting GreenGuile SMS Simulator")
    print("Type SMS commands or 'quit' to exit")
    print("Available commands: ACTIVATE, DEACTIVATE, SEASON <season>, STATUS")
    print("-" * 50)
    
    # Initialize system
    gg = GreenGuile()
    config = ConfigManager()
    sms = SMSHandler(gg)
    
    # Load sound patterns
    gg.load_sound_patterns("datasets/bird_sounds/")
    gg.update_season(config.get("season", "spring"))
    
    # Simulate receiving SMS commands
    while True:
        try:
            command = input("\nSMS Command: ")
            if command.lower() == 'quit':
                break
                
            response = sms.process_sms(command)
            print(f"Response: {response}")
            
        except KeyboardInterrupt:
            break
        except EOFError:
            break
            
    print("\nSMS Simulator shutting down...")


if __name__ == "__main__":
    simulate_sms_system()