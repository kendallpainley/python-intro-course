"""
Module 09 Exercises: Functions
================================
"""
print("=" * 55)
print("   Module 09 Exercises: Functions")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Temperature Converter Function
# Write a function celsius_to_fahrenheit(c) that converts
# Celsius to Fahrenheit (F = C * 9/5 + 32).
# Test it with 0, 100, -40, and 37.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: define celsius_to_fahrenheit and test it


# ──────────────────────────────────────────────────────────
# Exercise 2: Is Prime?
# Write is_prime(n) that returns True if n is prime, False otherwise.
# Test with: 2, 3, 4, 17, 25, 97
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: define is_prime and test it


# ──────────────────────────────────────────────────────────
# Exercise 3: Default Arguments
# Write greet(name, greeting="Hello", punctuation="!")
# that returns "<greeting>, <name><punctuation>"
# Test several combinations using keyword arguments.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
# TODO: define greet with defaults and test


# ──────────────────────────────────────────────────────────
# Exercise 4: *args — Statistics
# Write a function stats(*numbers) that prints:
#   count, sum, min, max, and average of the numbers passed.
# Test with stats(5, 10, 3, 8, 1, 7)
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
# TODO: define stats() with *args


# ──────────────────────────────────────────────────────────
# Exercise 5: Lambda Sorting
# Given the list of dictionaries below, sort by:
#   a) price (ascending)
#   b) name (alphabetical)
# Use sorted() with a lambda key.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 ]")
products = [
    {"name": "Widget", "price": 9.99},
    {"name": "Gadget", "price": 24.99},
    {"name": "Doohickey", "price": 4.99},
    {"name": "Thingamajig", "price": 14.99},
]
# TODO: sort by price then by name


# ──────────────────────────────────────────────────────────
# Exercise 6: Recursive Power
# Write power(base, exp) recursively (no ** operator allowed!)
# power(2, 10) should return 1024
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 6 ]")
# TODO: recursive power function


# ──────────────────────────────────────────────────────────
# Exercise 7 (Challenge): Memoized Fibonacci
# The naive recursive fibonacci is slow for large n.
# Use a dictionary as a cache to speed it up.
# Compute fibonacci(40) — should be 102334155
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 7 — Challenge ]")
# TODO: memoized fibonacci using a dict cache


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   def celsius_to_fahrenheit(c):
#       return c * 9 / 5 + 32
#   for temp in [0, 100, -40, 37]:
#       print(f"{temp}C = {celsius_to_fahrenheit(temp):.1f}F")
#
# SOLUTION 2:
#   def is_prime(n):
#       if n < 2: return False
#       for i in range(2, int(n**0.5)+1):
#           if n % i == 0: return False
#       return True
#   for n in [2,3,4,17,25,97]:
#       print(f"{n}: {is_prime(n)}")
#
# SOLUTION 3:
#   def greet(name, greeting="Hello", punctuation="!"):
#       return f"{greeting}, {name}{punctuation}"
#   print(greet("Alice"))
#   print(greet("Bob", greeting="Hi"))
#   print(greet("Carol", greeting="Hey", punctuation="..."))
#
# SOLUTION 4:
#   def stats(*numbers):
#       print(f"Count: {len(numbers)}")
#       print(f"Sum:   {sum(numbers)}")
#       print(f"Min:   {min(numbers)}")
#       print(f"Max:   {max(numbers)}")
#       print(f"Avg:   {sum(numbers)/len(numbers):.2f}")
#   stats(5, 10, 3, 8, 1, 7)
#
# SOLUTION 5:
#   by_price = sorted(products, key=lambda p: p["price"])
#   by_name  = sorted(products, key=lambda p: p["name"])
#   print(by_price)
#   print(by_name)
#
# SOLUTION 6:
#   def power(base, exp):
#       if exp == 0: return 1
#       return base * power(base, exp - 1)
#   print(power(2, 10))
#
# SOLUTION 7:
#   cache = {}
#   def fib(n):
#       if n in cache: return cache[n]
#       if n <= 1: return n
#       cache[n] = fib(n-1) + fib(n-2)
#       return cache[n]
#   print(fib(40))
