"""
SMS Communication Module for GreenGuile

Handles receiving commands via SMS to update system settings.
"""

import re


class SMSHandler:
    def __init__(self, green_guile_instance):
        """
        Initialize the SMS handler.
        
        Args:
            green_guile_instance (GreenGuile): The main GreenGuile instance
        """
        self.gg = green_guile_instance
        self.commands = {
            "ACTIVATE": self._activate,
            "DEACTIVATE": self._deactivate,
            "SEASON": self._set_season,
            "STATUS": self._status
        }
        
    def process_sms(self, sms_content):
        """
        Process an incoming SMS command.
        
        Args:
            sms_content (str): The content of the received SMS
        """
        # Parse the SMS content for commands
        command_parts = sms_content.strip().upper().split()
        if not command_parts:
            return "Invalid command format"
            
        command = command_parts[0]
        args = command_parts[1:] if len(command_parts) > 1 else []
        
        if command in self.commands:
            return self.commands[command](args)
        else:
            return f"Unknown command: {command}"
            
    def _activate(self, args):
        """Activate the GreenGuile system."""
        self.gg.activate()
        return "System activated"
        
    def _deactivate(self, args):
        """Deactivate the GreenGuile system."""
        self.gg.deactivate()
        return "System deactivated"
        
    def _set_season(self, args):
        """Set the current season."""
        if not args:
            return "SEASON command requires a season parameter"
            
        season = args[0].lower()
        valid_seasons = {"spring": "spring", "summer": "summer", 
                        "autumn": "autumn", "fall": "autumn",
                        "winter": "winter"}
                        
        if season in valid_seasons:
            self.gg.update_season(valid_seasons[season])
            return f"Season set to {valid_seasons[season]}"
        else:
            return f"Invalid season: {season}. Use spring/summer/autumn/winter"
            
    def _status(self, args):
        """Get system status."""
        status = f"GreenGuile Status:\\n"
        status += f"Active: {self.gg.is_active}\\n"
        status += f"Current Season: {self.gg.current_season}\\n"
        return status