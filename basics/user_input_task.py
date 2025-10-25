"""
ALX Client Welcome Program
Demonstrates: input(), type conversion, string formatting
"""

def welcome_user():
    name = input("Enter your name: ").strip()
    age = input("Enter your age: ").strip()
    
    if not age.isdigit():
        return "❌ Age must be numeric!"
    
    age = int(age)
    
    return f"👋 Hello {name}, you are {age} years old!"

if __name__ == "__main__":
    print(welcome_user())
