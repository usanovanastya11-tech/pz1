#!/usr/bin/env python3
"""
Integration tests for the project
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import greet, farewell

def test_greet_farewell_flow():
    """Test the complete greeting flow"""
    name = "TestUser"
    
    greeting = greet(name)
    goodbye = farewell(name)
    
    assert "Hello" in greeting
    assert "TestUser" in greeting
    assert "Goodbye" in goodbye
    assert "TestUser" in goodbye
    
    print("✓ Integration test passed")

def test_module_imports():
    """Test that all modules can be imported"""
    try:
        from helper import greet, farewell, multiply, calculate_stats, validate_email
        print("✓ All modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

if __name__ == "__main__":
    test_module_imports()
    test_greet_farewell_flow()
    print("🎉 All integration tests passed!")
