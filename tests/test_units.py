#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from helper import greet, farewell, multiply, power, calculate_stats, validate_email

def test_greet():
    assert greet("World") == "Hello, World!"
    print("test_greet passed")

def test_farewell():
    assert farewell("World") == "Goodbye, World!"
    print("test_farewell passed")

def test_multiply():
    assert multiply(2, 3) == 6
    print("test_multiply passed")

def test_power():
    assert power(2, 3) == 8
    print("test_power passed")

def test_calculate_stats():
    stats = calculate_stats([1, 2, 3, 4, 5])
    assert stats["mean"] == 3.0
    assert stats["min"] == 1
    assert stats["max"] == 5
    print("test_calculate_stats passed")

def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid-email") == False
    print("test_validate_email passed")

if __name__ == "__main__":
    test_greet()
    test_farewell()
    test_multiply()
    test_power()
    test_calculate_stats()
    test_validate_email()
    print("All unit tests passed!")
