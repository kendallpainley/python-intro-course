"""
Module 08 Exercises: For Loops
================================
"""
print("=" * 55)
print("   Module 08 Exercises: For Loops")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Sum with range()
# Use a for loop + range() to calculate the sum of all
# numbers from 1 to 50 (inclusive). Print the result.
# Expected: 1275
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: sum 1..50 with for loop


# ──────────────────────────────────────────────────────────
# Exercise 2: FizzBuzz with For
# Print numbers 1-20 using FizzBuzz rules (from Module 07)
# but this time use a for loop with range().
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: FizzBuzz 1-20 with for loop


# ──────────────────────────────────────────────────────────
# Exercise 3: Numbered List
# Use enumerate() to print the shopping list below, numbered
# starting from 1.
# Example:  1. eggs
#           2. milk  ...
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
shopping = ["eggs", "milk", "bread", "butter", "cheese"]
# TODO: use enumerate to print numbered list


# ──────────────────────────────────────────────────────────
# Exercise 4: Zip Score Report
# Pair up the names and scores below using zip().
# Print: "Alice scored 92/100"  for each student.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
students = ["Alice", "Bob", "Carol", "Dave"]
scores   = [92, 78, 88, 65]
# TODO: zip and print report


# ──────────────────────────────────────────────────────────
# Exercise 5: Nested Loop — Multiplication Table
# Print a 5x5 multiplication table using nested for loops.
# Format each cell as width-4 for alignment.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 ]")
# TODO: 5x5 multiplication table


# ──────────────────────────────────────────────────────────
# Exercise 6: Search and Break
# Given the list below, find the FIRST prime number in it.
# A prime is divisible only by 1 and itself.
# Print: "First prime: X"
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 6 ]")
numbers = [4, 6, 8, 9, 10, 7, 15, 11]
# TODO: find first prime using for + break


# ──────────────────────────────────────────────────────────
# Exercise 7 (Challenge): Flatten a 2D List
# Given a 2D list (list of lists), produce a flat 1D list
# using nested for loops.
# [[1,2],[3,4],[5,6]] → [1,2,3,4,5,6]
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 7 — Challenge ]")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = []
# TODO: flatten matrix into flat list


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   total = 0
#   for n in range(1, 51):
#       total += n
#   print(total)  # 1275
#
# SOLUTION 2:
#   for n in range(1, 21):
#       if n % 15 == 0:   print("FizzBuzz")
#       elif n % 3 == 0:  print("Fizz")
#       elif n % 5 == 0:  print("Buzz")
#       else:             print(n)
#
# SOLUTION 3:
#   for i, item in enumerate(shopping, start=1):
#       print(f"{i}. {item}")
#
# SOLUTION 4:
#   for name, score in zip(students, scores):
#       print(f"{name} scored {score}/100")
#
# SOLUTION 5:
#   for i in range(1, 6):
#       for j in range(1, 6):
#           print(f"{i*j:4}", end="")
#       print()
#
# SOLUTION 6:
#   def is_prime(n):
#       if n < 2: return False
#       for i in range(2, int(n**0.5)+1):
#           if n % i == 0: return False
#       return True
#   for n in numbers:
#       if is_prime(n):
#           print(f"First prime: {n}")
#           break
#   else:
#       print("No primes found")
#
# SOLUTION 7:
#   for row in matrix:
#       for item in row:
#           flat.append(item)
#   print(flat)
