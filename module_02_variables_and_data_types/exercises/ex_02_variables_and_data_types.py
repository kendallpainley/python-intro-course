"""
Module 02 Exercises: Variables & Data Types
============================================
"""
print("=" * 55)
print("   Module 02 Exercises: Variables & Data Types")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Create Variables
# Create ONE variable of each type: int, float, str, bool, NoneType
# Print each variable AND its type on the same line.
# Expected format:  42 <class 'int'>
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: create 5 variables and print each with its type


# ──────────────────────────────────────────────────────────
# Exercise 2: Personal Profile
# Create variables for: your name, age, height (in meters),
# whether you are a student, and your favourite_color.
# Then print a formatted summary using those variables.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: create profile variables, then print a summary


# ──────────────────────────────────────────────────────────
# Exercise 3: Tuple Unpacking
# Assign the values 10, 20, 30 to variables x, y, z
# using a SINGLE line of code. Then print them.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
# TODO: one-line multiple assignment


# ──────────────────────────────────────────────────────────
# Exercise 4: Variable Swap
# a = 100, b = 200
# Swap their values WITHOUT using a third variable.
# Print before and after.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
a = 100
b = 200
print(f"Before: a={a}, b={b}")
# TODO: swap a and b in one line
# print(f"After:  a={a}, b={b}")   # uncomment after your swap


# ──────────────────────────────────────────────────────────
# Exercise 5: Type Detective
# Given the variables below, print a sentence describing each one.
# Format: "x is a <type> with value <value>"
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 ]")
mystery_1 = 3.14
mystery_2 = "Python"
mystery_3 = 99
mystery_4 = False
mystery_5 = None
# TODO: print a description for each mystery variable


# ──────────────────────────────────────────────────────────
# Exercise 6 (Challenge): Dynamic Typing
# Create a variable called "shape_shifter", assign it an int,
# print it with its type. Then reassign it to a str, print again.
# Then reassign to a bool, print again. Observe how type changes!
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 6 — Challenge ]")
# TODO: demonstrate dynamic typing


print("\n" + "=" * 55)
print("Done! Check your output.")
print("=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   my_int = 42
#   my_float = 3.14
#   my_str = "hello"
#   my_bool = True
#   my_none = None
#   print(my_int, type(my_int))
#   print(my_float, type(my_float))
#   print(my_str, type(my_str))
#   print(my_bool, type(my_bool))
#   print(my_none, type(my_none))
#
# SOLUTION 2:
#   name = "Alex"
#   age = 25
#   height = 1.75
#   is_student = True
#   favourite_color = "blue"
#   print("Name:", name)
#   print("Age:", age)
#   print("Height:", height, "m")
#   print("Student:", is_student)
#   print("Favourite color:", favourite_color)
#
# SOLUTION 3:
#   x, y, z = 10, 20, 30
#   print(x, y, z)
#
# SOLUTION 4:
#   a, b = b, a
#   print(f"After:  a={a}, b={b}")
#
# SOLUTION 5:
#   print(f"mystery_1 is a {type(mystery_1).__name__} with value {mystery_1}")
#   print(f"mystery_2 is a {type(mystery_2).__name__} with value {mystery_2}")
#   print(f"mystery_3 is a {type(mystery_3).__name__} with value {mystery_3}")
#   print(f"mystery_4 is a {type(mystery_4).__name__} with value {mystery_4}")
#   print(f"mystery_5 is a {type(mystery_5).__name__} with value {mystery_5}")
#
# SOLUTION 6:
#   shape_shifter = 100
#   print(shape_shifter, type(shape_shifter))
#   shape_shifter = "one hundred"
#   print(shape_shifter, type(shape_shifter))
#   shape_shifter = True
#   print(shape_shifter, type(shape_shifter))
