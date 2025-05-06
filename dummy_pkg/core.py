"""
Core functionality of the dummy package.
This module doesn't actually do anything useful.
"""

def hello_world():
    """A function that returns a greeting."""
    return "Hello from the dummy package!"

def add_numbers(a, b):
    """A simple function that adds two numbers."""
    return a + b

# This class doesn't do anything useful
class DummyClass:
    """A class that doesn't do much."""
    
    def __init__(self, name="Dummy"):
        self.name = name
    
    def get_name(self):
        """Returns the name."""
        return self.name
    
    def set_name(self, name):
        """Sets the name."""
        self.name = name
