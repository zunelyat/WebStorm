# test_webstormjs.py
"""
Tests for WebStormJS module.
"""

import unittest
from webstormjs import WebStormJS

class TestWebStormJS(unittest.TestCase):
    """Test cases for WebStormJS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WebStormJS()
        self.assertIsInstance(instance, WebStormJS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WebStormJS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
