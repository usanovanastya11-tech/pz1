#!/usr/bin/env python3

from helper import greet, farewell, power, calculate_stats, validate_email

def main():
    print("Hello from main.py - Version 1.1.0")
    print(greet("User"))
    print(farewell("User"))

    # Demonstrate power function
    result = power(2, 3)
    print(f"2^3 = {result}")

    # Demonstrate stats function
    numbers = [1, 2, 3, 4, 5]
    stats = calculate_stats(numbers)
    print(f"Stats for {numbers}: {stats}")

    # Demonstrate email validation
    emails = ["test@example.com", "invalid-email"]
    for email in emails:
        is_valid = validate_email(email)
        print(f"Email '{email}' is valid: {is_valid}")

if __name__ == "__main__":
    main()
