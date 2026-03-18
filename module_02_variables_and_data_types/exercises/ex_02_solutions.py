"""
Module 02 Exercises: Variables & Data Types — SOLUTIONS
========================================================
"""

# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝


# ─────────────────────────────────────────────
# EXERCISE: Create Variables
# ─────────────────────────────────────────────
print("\n[ Exercise 1 ]")

my_int   = 42
my_float = 3.14
my_str   = "hello"
my_bool  = True
my_none  = None

print(my_int,   type(my_int))
print(my_float, type(my_float))
print(my_str,   type(my_str))
print(my_bool,  type(my_bool))
print(my_none,  type(my_none))


# ─────────────────────────────────────────────
# EXERCISE: Personal Profile
# ─────────────────────────────────────────────
print("\n[ Exercise 2 ]")

name = "Alex"
age = 25
height = 1.75
is_student = True
favorite_color = "blue"

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)
print("Favorite color:", favorite_color)


# ─────────────────────────────────────────────
# EXERCISE: Tuple Unpacking
# ─────────────────────────────────────────────
print("\n[ Exercise 3 ]")

x, y, z = 10, 20, 30
print(x, y, z)


# ─────────────────────────────────────────────
# EXERCISE: Variable Swap
# ─────────────────────────────────────────────
print("\n[ Exercise 4 ]")

a = 100
b = 200
print(f"Before: a={a}, b={b}")

a, b = b, a

print(f"After:  a={a}, b={b}")


# ─────────────────────────────────────────────
# EXERCISE: Type Detective
# ─────────────────────────────────────────────
print("\n[ Exercise 5 ]")

mystery_1 = 3.14
mystery_2 = "Python"
mystery_3 = 99
mystery_4 = False
mystery_5 = None


print(f"mystery_1 is a {type(mystery_1)} with value {mystery_1}")
print(f"mystery_2 is a {type(mystery_2)} with value {mystery_2}")
print(f"mystery_3 is a {type(mystery_3)} with value {mystery_3}")
print(f"mystery_4 is a {type(mystery_4)} with value {mystery_4}")
print(f"mystery_5 is a {type(mystery_5)} with value {mystery_5}")


# ─────────────────────────────────────────────
# EXERCISE: Dynamic Typing
# ─────────────────────────────────────────────
print("\n[ Exercise 6 ]")

shape_shifter = 100
print(shape_shifter, type(shape_shifter))

shape_shifter = "one hundred"
print(shape_shifter, type(shape_shifter))

shape_shifter = True
print(shape_shifter, type(shape_shifter))




# ─────────────────────────────────────────────
# EXERCISE: Temperature Converter
# ─────────────────────────────────────────────
print("\n[ Exercise 7 ]")

celsius = 100.0
fahrenheit = (celsius * 9 / 5) + 32
fahrenheit = round(fahrenheit, 1)

print(f"{celsius}°C = {fahrenheit}°F")

# Try a few more to sanity-check:
# 0°C → 32°F  (freezing)
# 37°C → 98.6°F  (body temperature)


# ─────────────────────────────────────────────
# EXERCISE: Fix the Bug
# ─────────────────────────────────────────────
print("\n[ Exercise 8 ]")

user_age = "25"
years_until_30 = 30 - int(user_age)   # int() converts "25" → 25
print(f"Years until 30: {years_until_30}")

# Why does it crash without int()?
# Python can't subtract a str from an int — they're different types.
# The fix is to convert the string to an int first using int().

