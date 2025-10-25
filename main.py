print("Hello from main.py - Version 1.1.0")

from helper import greet, farewell, power, is_prime

def main():
    print(greet("User"))
    print(farewell("User"))
    
    power_result = power(2, 8)
    print(f"2^8 = {power_result}")
    
    prime_check = is_prime(17)
    print(f"Is 17 prime? {prime_check}")

if __name__ == "__main__":
    main()
