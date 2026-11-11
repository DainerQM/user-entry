"""Simple examples of terminal input, type conversion, and f-strings.

Run this file with:
    python user_input_examples.py
"""

print("PYTHON USER INPUT")
print("-----------------")
print("Type an answer and press Enter after each question.")

name = input("\nWhat is your name? ").strip()
age_text = input("How old are you? ")
height_text = input("How tall are you in meters? ")

print("\n1. INPUT STARTS AS TEXT")
print(f"Your name is stored as: {name!r}")
print(f"The age response is text: {age_text!r}")
print("Type of the age response:", type(age_text))

print("\n2. CONVERT TEXT TO NUMBERS")
age = int(age_text)
height = float(height_text)
print("Converted age:", age, type(age))
print("Converted height:", height, type(height))

print("\n3. FORMAT THE RESULTS WITH F-STRINGS")
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Next year, you will be {age + 1}.")
print(f"Your height is {height:.2f} meters.")
print(f"F-strings can also display literal braces: {{ and }}.")
