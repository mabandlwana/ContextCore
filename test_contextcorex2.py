# test_contextcorex2.py
"""
Tests for ContextCoreX2 module.
"""

import unittest
from contextcorex2 import ContextCoreX2

class TestContextCoreX2(unittest.TestCase):
    """Test cases for ContextCoreX2 class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ContextCoreX2()
        self.assertIsInstance(instance, ContextCoreX2)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ContextCoreX2()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
