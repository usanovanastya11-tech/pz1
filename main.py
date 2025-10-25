print("Hello from main.py - CONFLICTING CHANGE IN MAIN!")
def farewell(name):
    return f"Goodbye, {name}!"

print("Hello from main.py - modified by person1 in dev branch - DIFFERENT TEXT!")
def new_function():
    return "This is a new function"

print("Additional line added by person2 in dev2 branch")

print("Hello from main.py - merged version after conflict resolution")
def new_function():
    return "This is a new function"

print("Hell from main.py!")

from helper import greet, farewell

def main():
    print(greet("User"))
    print(farewell("User"))

if __name__ == "__main__":
    main()

