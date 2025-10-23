
# Mini Project: Simple Calculator


# 🔧 Project Description

# Build a calculator that:

# Takes two numbers from the user

# Asks what operation to perform (+, -, *, /)

# Displays the result neatly


# ------------------------------------------------------------------------------------------


print("=== Simple Calculator ===")

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Choose operation
operation = input("Choose operation (+, -, *, /): ")

# Perform calculation
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
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

# Display result
print(f"Result: {result}")




# ===============================================================================

# Try It Yourself:

# Add more operations like exponentiation (**) or modulus (%).

# Use round(result, 2) to round results.

# Allow multiple calculations until the user types "exit".