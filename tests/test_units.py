#!/usr/bin/env python3
"""
Unit tests for the project
"""
import sys
import os

# Добавляем путь к корню проекта для импорта
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import greet, farewell, multiply, calculate_stats, validate_email

def test_greet():
    """Test greet function"""
    assert greet("World") == "Hello, World!"
    assert greet("") == "Hello, !"
    print("✓ test_greet passed")

def test_farewell():
    """Test farewell function"""
    assert farewell("World") == "Goodbye, World!"
    assert farewell("") == "Goodbye, !"
    print("✓ test_farewell passed")

def test_multiply():
    """Test multiply function"""
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-1, 5) == -5
    print("✓ test_multiply passed")

def test_calculate_stats():
    """Test statistics calculation"""
    result = calculate_stats([1, 2, 3, 4, 5])
    assert result["count"] == 5
    assert result["sum"] == 15
    assert result["average"] == 3.0
    
    # Test empty list
    result_empty = calculate_stats([])
    assert result_empty["count"] == 0
    assert result_empty["sum"] == 0
    assert result_empty["average"] == 0
    print("✓ test_calculate_stats passed")

def test_validate_email():
    """Test email validation"""
    assert validate_email("test@example.com") == True
    assert validate_email("user.name@domain.co.uk") == True
    assert validate_email("invalid") == False
    assert validate_email("missing@domain") == False
    assert validate_email("") == False
    print("✓ test_validate_email passed")

if __name__ == "__main__":
    test_greet()
    test_farewell()
    test_multiply()
    test_calculate_stats()
    test_validate_email()
    print("🎉 All unit tests passed!")

def test_power():
    from helper import power
    assert power(2, 3) == 8
    print("test_power passed")

if __name__ == "__main__":
    test_greet()
    test_farewell()
    test_multiply()
    test_power()
    print("All unit tests passed!")

def test_is_prime():
    from helper import is_prime
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(1) == False
    print("test_is_prime passed")

if __name__ == "__main__":
    test_greet()
    test_farewell()
    test_multiply()
    test_power()
    test_is_prime()
    print("All unit tests passed!")
