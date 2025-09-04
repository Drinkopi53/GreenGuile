"""
Main Application for GreenGuile

Acoustic pest deterrent system using predator sound patterns.
Optimized for microcontroller usage.
"""

import time
import gc
from green_guile import GreenGuile
from sms_handler import SMSHandler
from config import ConfigManager


def is_within_active_hours(start_time, end_time):
    """
    Check if current time is within active hours.
    
    Args:
        start_time (str): Start time in HH:MM format
        end_time (str): End time in HH:MM format
        
    Returns:
        bool: True if current time is within active hours
    """
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    
    start_parts = start_time.split(":")
    end_parts = end_time.split(":")
    
    start_hour = int(start_parts[0])
    start_minute = int(start_parts[1])
    end_hour = int(end_parts[0])
    end_minute = int(end_parts[1])
    
    current_total_minutes = current_hour * 60 + current_minute
    start_total_minutes = start_hour * 60 + start_minute
    end_total_minutes = end_hour * 60 + end_minute
    
    return start_total_minutes <= current_total_minutes <= end_total_minutes


def main():
    """Main application entry point."""
    print("Starting GreenGuile - Acoustic Pest Deterrent System")
    print("Optimized for microcontroller usage")
    
    # Initialize components
    gg = GreenGuile()
    config = ConfigManager()
    sms = SMSHandler(gg)
    
    # Load sound patterns
    gg.load_sound_patterns("datasets/bird_sounds/")
    
    # Set initial season from config
    gg.update_season(config.get("season", "spring"))
    
    # Activate the system
    gg.activate()
    
    print("GreenGuile is running. Send SMS commands to control the system.")
    print("Available commands: ACTIVATE, DEACTIVATE, SEASON <season>, STATUS")
    
    # Get configuration
    sound_interval = config.get("sound_interval", 300)  # Default 5 minutes
    active_hours = config.get("active_hours", {"start": "06:00", "end": "18:00"})
    
    # Main loop
    last_sound_time = 0
    last_gc_time = time.time()
    
    try:
        while True:
            current_time = time.time()
            
            # Perform periodic garbage collection to optimize memory
            if (current_time - last_gc_time) >= 60:  # Every minute
                gc.collect()
                last_gc_time = current_time
            
            # Check if system is active and within active hours
            if (gg.is_active and 
                is_within_active_hours(active_hours["start"], active_hours["end"])):
                
                # Check if it's time to play a sound
                if (current_time - last_sound_time) >= sound_interval:
                    gg.run_cycle()
                    last_sound_time = current_time
                
            # In a real implementation, we would check for incoming SMS here
            # For simulation, we'll just sleep
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutting down GreenGuile...")
        gg.deactivate()
        print("GreenGuile has been shut down.")


if __name__ == "__main__":
    main()