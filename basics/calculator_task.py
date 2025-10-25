def calculator():
    print("\n📌 Simple Python Calculator\n")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ").strip()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                return "❌ Error: Cannot divide by zero."
        else:
            return "❌ Invalid operation!"
        
        return f"✅ Result: {result}"
    
    except ValueError:
        return "❌ Invalid numeric input!"

if __name__ == "__main__":
    print(calculator())
