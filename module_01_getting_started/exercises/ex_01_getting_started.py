"""
Module 01 Exercises: Getting Started with Python
=================================================
Instructions:
  1. Write your code below each TODO comment
  2. Run the file:  python ex_01_getting_started.py
  3. Only scroll to the SOLUTIONS section after you have tried each exercise!
"""

print("=" * 55)
print("   Module 01 Exercises: Getting Started")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Hello, World!
# Print the classic greeting: Hello, World!
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
print("Hello, World!")


# ──────────────────────────────────────────────────────────
# Exercise 2: Personal Introduction
# Use THREE separate print() calls to output:
#   My name is [your name].
#   I am [your age] years old.
#   I am learning Python!
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
print("My name is KJ")
print("I am 25 years old.")
print("I am learning Python!")


# ──────────────────────────────────────────────────────────
# Exercise 3: Add Meaningful Comments
# The code below works but has zero comments.
# Add a descriptive comment above EACH print() explaining what it does.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
# Prints Python is fun!
print("Python is fun!")
# Prints I am becoming a programmer!
print("I am becoming a programmer!")
# Prints nothing, serves as a blank space
print()
# Prints See you in the next module!
print("See you in the next module!")


# ──────────────────────────────────────────────────────────
# Exercise 4: Custom Separator
# Print the words "Python", "is", "great" on ONE line
# separated by " --> " using the sep= parameter.
# Expected output:  Python --> is --> great
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
print("Python", "is", "great", sep=" --> ")


# ──────────────────────────────────────────────────────────
# Exercise 5: Same-line Printing
# Use TWO print() statements that together produce ONE line of output:
#   Hello World!
# Hint: use end= on the first print()
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 ]")
print("Hello", end=" ")
print("World!")


# ──────────────────────────────────────────────────────────
# Exercise 6: Debug This Code (3 errors to find and fix)
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 6 ]")
# Fix the three errors below (uncomment and correct each line):
print("Hello from Python!")
print("I love coding!")
print("Python is case-sensitive!")


# ──────────────────────────────────────────────────────────
# Exercise 7 (Challenge): ASCII Art Box
# Use print() to draw this box exactly:
#   +---------+
#   |  Hello  |
#   +---------+
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 7 — Challenge ]")
print("+---------+")
print("|  Hello  |")
print("+---------+")


print("\n" + "=" * 55)
print("Done! Review your output above.")
print("=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║                                                          ║
# ║        !! SOLUTIONS — STOP SCROLLING IF YOU             ║
# ║           HAVEN'T TRIED THE EXERCISES YET !!            ║
# ║                                                          ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   print("Hello, World!")
#
# SOLUTION 2:
#   print("My name is Alex.")
#   print("I am 25 years old.")
#   print("I am learning Python!")
#
# SOLUTION 3:
#   # Print an encouraging statement about Python
#   print("Python is fun!")
#   # Affirm our identity as a programmer
#   print("I am becoming a programmer!")
#   # Print a blank line for visual spacing
#   print()
#   # Say goodbye until the next module
#   print("See you in the next module!")
#
# SOLUTION 4:
#   print("Python", "is", "great", sep=" --> ")
#
# SOLUTION 5:
#   print("Hello ", end="")
#   print("World!")
#
# SOLUTION 6:
#   print("Hello from Python!")        # Fixed: Print → print
#   print("I love coding!")            # Fixed: missing closing quote
#   print("Python is case-sensitive!") # Fixed: removed leading space
#
# SOLUTION 7:
#   print("+---------+")
#   print("|  Hello  |")
#   print("+---------+")
