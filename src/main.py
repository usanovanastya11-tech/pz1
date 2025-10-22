#!/usr/bin/env python3

from helper import greet, farewell, power

def main():
    print("Hello from main.py - Version 1.0.0")
    print(greet("User"))
    print(farewell("User"))
    result = power(2, 3)
    print(f"2^3 = {result}")

if __name__ == "__main__":
    main()
