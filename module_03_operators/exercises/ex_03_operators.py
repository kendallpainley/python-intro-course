"""
Module 03 Exercises: Operators
================================
"""
print("=" * 55)
print("   Module 03 Exercises: Operators")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Arithmetic Calculator
# Given a = 17 and b = 5, print the result of:
#   a + b, a - b, a * b, a / b, a // b, a % b, a ** b
# Label each result clearly.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
a = 17
b = 5
# TODO: print each arithmetic result with a label


# ──────────────────────────────────────────────────────────
# Exercise 2: Time Converter
# Convert 500 minutes into hours and remaining minutes.
# Expected: "500 minutes = 8 hours and 20 minutes"
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
total_minutes = 500
# TODO: calculate hours and remaining minutes, then print


# ──────────────────────────────────────────────────────────
# Exercise 3: Even or Odd Detector
# Use the modulo operator to determine:
#   Is 47 even? Is 82 even? Print True/False for each.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
# TODO: use % to check even/odd (even if n % 2 == 0)


# ──────────────────────────────────────────────────────────
# Exercise 4: Comparisons
# Set x = 15. Print the result of each comparison:
#   x > 10, x == 15, x != 20, x <= 15, x >= 16
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
x = 15
# TODO: print 5 comparison results


# ──────────────────────────────────────────────────────────
# Exercise 5: Access Control
# Given: age = 17, has_parent_permission = True
# Can the user watch an R-rated film?
# Rule: must be 18+ OR have parent permission
# Print: "Access granted" or "Access denied"
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 ]")
age = 17
has_parent_permission = True
# TODO: use logical operators to decide access


# ──────────────────────────────────────────────────────────
# Exercise 6: Assignment Operators
# Start with points = 50. Apply these changes in order:
#   Add 25, subtract 10, multiply by 3, floor divide by 4
# Print points after EACH operation.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 6 ]")
points = 50
# TODO: use +=, -=, *=, //= and print after each


# ──────────────────────────────────────────────────────────
# Exercise 7 (Challenge): Quadratic Formula
# Compute both roots of: 2x² + 5x - 3 = 0
# Formula: x = (-b ± sqrt(b²-4ac)) / 2a
# Hint: square root = ** 0.5
# a=2, b=5, c=-3  → roots should be 0.5 and -3.0
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 7 — Challenge ]")
a, b, c = 2, 5, -3
# TODO: calculate and print both roots


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   print(f"a + b = {a + b}")
#   print(f"a - b = {a - b}")
#   print(f"a * b = {a * b}")
#   print(f"a / b = {a / b}")
#   print(f"a // b = {a // b}")
#   print(f"a % b = {a % b}")
#   print(f"a ** b = {a ** b}")
#
# SOLUTION 2:
#   hours = total_minutes // 60
#   mins = total_minutes % 60
#   print(f"{total_minutes} minutes = {hours} hours and {mins} minutes")
#
# SOLUTION 3:
#   print(f"Is 47 even? {47 % 2 == 0}")
#   print(f"Is 82 even? {82 % 2 == 0}")
#
# SOLUTION 4:
#   print(x > 10, x == 15, x != 20, x <= 15, x >= 16)
#
# SOLUTION 5:
#   can_watch = age >= 18 or has_parent_permission
#   print("Access granted" if can_watch else "Access denied")
#
# SOLUTION 6:
#   points += 25;  print(points)   # 75
#   points -= 10;  print(points)   # 65
#   points *= 3;   print(points)   # 195
#   points //= 4;  print(points)   # 48
#
# SOLUTION 7:
#   discriminant = b**2 - 4*a*c
#   root1 = (-b + discriminant**0.5) / (2*a)
#   root2 = (-b - discriminant**0.5) / (2*a)
#   print(f"Root 1: {root1}")
#   print(f"Root 2: {root2}")
