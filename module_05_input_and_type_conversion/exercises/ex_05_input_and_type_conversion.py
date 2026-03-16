"""
Module 05 Exercises: User Input & Type Conversion
===================================================
Note: These exercises use input() — run from the terminal, not a notebook cell,
for the best interactive experience.
"""
print("=" * 55)
print("   Module 05 Exercises: Input & Type Conversion")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Name and Age
# Ask the user for their name and year of birth.
# Calculate and print their age (use 2024 as current year).
# Print: "Hello Alice! You are approximately 30 years old."
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: get name and birth year, calculate age, print result


# ──────────────────────────────────────────────────────────
# Exercise 2: Temperature Converter
# Ask for a temperature in Celsius.
# Convert and print it in Fahrenheit.
# Formula: F = C * 9/5 + 32
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: get Celsius, convert to Fahrenheit, print with 1 decimal place


# ──────────────────────────────────────────────────────────
# Exercise 3: Truthy/Falsy Explorer
# For each value below, print whether it is truthy or falsy.
# Format: "0 is falsy"  or  "42 is truthy"
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
values = [0, 1, -5, "", "hello", None, [], [0], 0.0, 0.001]
# TODO: loop through values and print truthy/falsy label


# ──────────────────────────────────────────────────────────
# Exercise 4: Rectangle Calculator
# Ask for width and height of a rectangle (as floats).
# Print the area and perimeter, each to 2 decimal places.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
# TODO: get width and height, calculate and print area & perimeter


# ──────────────────────────────────────────────────────────
# Exercise 5 (Challenge): Multi-step Converter
# Ask user to enter a number of seconds.
# Convert to hours, minutes, and remaining seconds.
# Example: 3725 seconds → "1h 2m 5s"
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 — Challenge ]")
# TODO: get seconds, break into h/m/s, print formatted


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   name = input("Your name: ")
#   birth_year = int(input("Year of birth: "))
#   age = 2024 - birth_year
#   print(f"Hello {name}! You are approximately {age} years old.")
#
# SOLUTION 2:
#   celsius = float(input("Temperature in Celsius: "))
#   fahrenheit = celsius * 9 / 5 + 32
#   print(f"{celsius}°C = {fahrenheit:.1f}°F")
#
# SOLUTION 3:
#   for v in values:
#       label = "truthy" if v else "falsy"
#       print(f"{repr(v)} is {label}")
#
# SOLUTION 4:
#   width = float(input("Width: "))
#   height = float(input("Height: "))
#   area = width * height
#   perimeter = 2 * (width + height)
#   print(f"Area:      {area:.2f}")
#   print(f"Perimeter: {perimeter:.2f}")
#
# SOLUTION 5:
#   total = int(input("Enter seconds: "))
#   hours = total // 3600
#   mins = (total % 3600) // 60
#   secs = total % 60
#   print(f"{total}s → {hours}h {mins}m {secs}s")
