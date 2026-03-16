"""
Module 17 Exercises: Comprehensions
======================================
"""
print("=" * 55)
print("   Module 17 Exercises: Comprehensions")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Rewrite with Comprehensions
# Convert each for loop below to a one-line comprehension.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")

# a) Cubes of odd numbers 1-19
cubes_of_odds = []
for n in range(1, 20):
    if n % 2 != 0:
        cubes_of_odds.append(n ** 3)
# TODO: rewrite as list comprehension

# b) Lower-case words longer than 3 chars
words = ["The", "quick", "BROWN", "fox", "JUMPS", "over"]
result_b = []
for w in words:
    if len(w) > 3:
        result_b.append(w.lower())
# TODO: rewrite as list comprehension

# c) Dict: word → length, for words of length > 3
result_c = {}
for w in words:
    if len(w) > 3:
        result_c[w.lower()] = len(w)
# TODO: rewrite as dict comprehension


# ──────────────────────────────────────────────────────────
# Exercise 2: Matrix Operations
# Use comprehensions to:
#   a) Transpose a 3x4 matrix (rows become columns)
#   b) Create a 5x5 identity matrix (1s on diagonal, 0s elsewhere)
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# TODO: a) transpose b) identity matrix


# ──────────────────────────────────────────────────────────
# Exercise 3: Data Processing with Dict Comprehension
# Given the list of (name, score) tuples, create:
#   a) A dict {name: grade_letter}  using A/B/C/D/F rules
#   b) A dict of ONLY students who passed (score >= 60)
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
results = [("Alice",92),("Bob",74),("Carol",88),("Dave",55),("Eve",61)]
# TODO: grade dict and passing dict comprehensions


# ──────────────────────────────────────────────────────────
# Exercise 4: Generator vs List Memory
# Create both a list comprehension and generator expression
# for squares of numbers 1 to 1,000,000.
# Use sys.getsizeof() to compare their memory size.
# Then compute the sum using the generator (not the list).
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
import sys
# TODO: compare memory and compute sum with generator


# ──────────────────────────────────────────────────────────
# Exercise 5 (Challenge): Sieve of Eratosthenes
# Generate all prime numbers up to 100 using comprehensions.
# Hint: n is prime if no m in range(2, n) divides it.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 — Challenge ]")
# TODO: sieve using comprehensions


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   a) cubes_of_odds = [n**3 for n in range(1,20) if n%2!=0]
#   b) result_b = [w.lower() for w in words if len(w)>3]
#   c) result_c = {w.lower():len(w) for w in words if len(w)>3}
#
# SOLUTION 2:
#   a) transposed = [[matrix[r][c] for r in range(3)] for c in range(4)]
#   b) identity = [[1 if i==j else 0 for j in range(5)] for i in range(5)]
#
# SOLUTION 3:
#   def grade(s):
#       if s>=90: return "A"
#       elif s>=80: return "B"
#       elif s>=70: return "C"
#       elif s>=60: return "D"
#       return "F"
#   grades = {n: grade(s) for n,s in results}
#   passing = {n: s for n,s in results if s>=60}
#   print(grades); print(passing)
#
# SOLUTION 4:
#   lst = [n**2 for n in range(1,1_000_001)]
#   gen = (n**2 for n in range(1,1_000_001))
#   print(f"List size: {sys.getsizeof(lst):,} bytes")
#   print(f"Gen size:  {sys.getsizeof(gen)} bytes")
#   print(f"Sum: {sum(n**2 for n in range(1,1_000_001))}")
#
# SOLUTION 5:
#   primes = [n for n in range(2,101) if all(n%m!=0 for m in range(2,n))]
#   print(primes)
