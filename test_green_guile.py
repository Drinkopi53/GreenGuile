"""
Test file for GreenGuile system
"""

import unittest
import time
from green_guile import GreenGuile
from sms_handler import SMSHandler
from config import ConfigManager


class TestGreenGuile(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.gg = GreenGuile()
        self.sms = SMSHandler(self.gg)
        self.config = ConfigManager("test_config.json")
        
    def test_initialization(self):
        """Test system initialization."""
        self.assertFalse(self.gg.is_active)
        self.assertEqual(self.gg.current_season, "spring")
        
    def test_sound_pattern_loading(self):
        """Test loading sound patterns."""
        self.gg.load_sound_patterns("test/path")
        self.assertIn("spring", self.gg.sound_patterns)
        self.assertIn("summer", self.gg.sound_patterns)
        
    def test_activation(self):
        """Test system activation."""
        self.gg.activate()
        self.assertTrue(self.gg.is_active)
        
    def test_deactivation(self):
        """Test system deactivation."""
        self.gg.activate()
        self.gg.deactivate()
        self.assertFalse(self.gg.is_active)
        
    def test_sms_commands(self):
        """Test SMS command processing."""
        # Test activation command
        response = self.sms.process_sms("ACTIVATE")
        self.assertEqual(response, "System activated")
        self.assertTrue(self.gg.is_active)
        
        # Test deactivation command
        response = self.sms.process_sms("DEACTIVATE")
        self.assertEqual(response, "System deactivated")
        self.assertFalse(self.gg.is_active)
        
        # Test season command
        response = self.sms.process_sms("SEASON summer")
        self.assertEqual(response, "Season set to summer")
        self.assertEqual(self.gg.current_season, "summer")
        
        # Test status command
        self.gg.activate()
        response = self.sms.process_sms("STATUS")
        self.assertIn("Active: True", response)
        self.assertIn("Current Season: summer", response)
        
    def test_config_manager(self):
        """Test configuration management."""
        # Test setting and getting config values
        self.config.set("test_value", 42)
        self.assertEqual(self.config.get("test_value"), 42)
        
        # Test default values
        self.assertEqual(self.config.get("nonexistent", "default"), "default")


if __name__ == "__main__":
    unittest.main()