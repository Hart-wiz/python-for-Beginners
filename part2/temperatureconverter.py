
# Mini Project: Temperature Converter

# Project Description
# Create a program that converts temperatures between Celsius and Fahrenheit using functions.

# _______________________________________________________________________________________________



def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("=== Temperature Converter ===")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose (1/2): ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f:.2f}°F")

elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F = {c:.2f}°C")

else:
    print("Invalid choice.")



# =============================================================================

# Try It Yourself
# Add a loop so users can perform multiple conversions.
# Round results to one decimal place.
# Add conversion for Kelvin.
# Let the program detect input unit automatically (e.g., 36C or 100F).



# 🧩 Quick Quiz

# What’s the difference between defining and calling a function?
# What is a parameter? What is an argument?
# What does the return keyword do?
# What’s the difference between a local and a global variable?
# Write a function multiply(x, y) that returns their product.