#!/usr/bin/env python3

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

def multiply(a, b):
    return a * b

def power(base, exponent):
    return base ** exponent

def calculate_stats(numbers):
    """Calculate basic statistics for a list of numbers"""
    if not numbers:
        return {"mean": 0, "min": 0, "max": 0}
    return {
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

def validate_email(email):
    """Basic email validation"""
    if "@" in email and "." in email:
        return True
    return False
