"""
Module 10 Exercises: Lists
============================
"""
print("=" * 55)
print("   Module 10 Exercises: Lists")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: List Manipulation
# Start with numbers = [5, 3, 8, 1, 9, 2, 7, 4, 6]
# a) Print the first 3 and last 3 elements
# b) Sort the list and print it
# c) Print the list reversed WITHOUT modifying original
# d) Print the sum, min, and max
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
numbers = [5, 3, 8, 1, 9, 2, 7, 4, 6]
# TODO: a, b, c, d


# ──────────────────────────────────────────────────────────
# Exercise 2: Building Lists
# Use a for loop to build two lists:
#   squares: squares of 1-10
#   evens:   even numbers from 1-20
# Print both.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: build squares and evens with for loops


# ──────────────────────────────────────────────────────────
# Exercise 3: Remove Duplicates
# Given: dupes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Create a new list with duplicates removed, preserving order.
# Expected: [3, 1, 4, 5, 9, 2, 6]
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
dupes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# TODO: remove duplicates preserving order


# ──────────────────────────────────────────────────────────
# Exercise 4: 2D Matrix Operations
# Given the 3x3 matrix below:
#   a) Print the diagonal (top-left to bottom-right)
#   b) Print the sum of all elements
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# TODO: diagonal and total sum


# ──────────────────────────────────────────────────────────
# Exercise 5: Stack Operations
# A stack is a list where you only add/remove from the end.
# Simulate a browser history stack:
#   - Visit 5 pages (push URLs)
#   - Go back 2 times (pop)
#   - Print current page (top of stack)
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 ]")
# TODO: browser history simulation


# ──────────────────────────────────────────────────────────
# Exercise 6 (Challenge): Rotate a List
# Write rotate(lst, k) that rotates a list left by k positions.
# rotate([1,2,3,4,5], 2) → [3,4,5,1,2]
# Use slicing — no loops needed!
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 6 — Challenge ]")
# TODO: rotate function using slicing


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   print(numbers[:3], numbers[-3:])
#   sorted_nums = sorted(numbers); print(sorted_nums)
#   print(numbers[::-1])
#   print(sum(numbers), min(numbers), max(numbers))
#
# SOLUTION 2:
#   squares = []
#   for n in range(1, 11): squares.append(n**2)
#   evens = []
#   for n in range(1, 21):
#       if n % 2 == 0: evens.append(n)
#   print(squares); print(evens)
#
# SOLUTION 3:
#   seen = []
#   for n in dupes:
#       if n not in seen: seen.append(n)
#   print(seen)
#
# SOLUTION 4:
#   diag = [matrix[i][i] for i in range(3)]; print(diag)
#   total = sum(matrix[i][j] for i in range(3) for j in range(3))
#   print(total)
#
# SOLUTION 5:
#   history = []
#   pages = ["home","about","products","contact","checkout"]
#   for p in pages: history.append(p); print(f"Visited: {p}")
#   history.pop(); print("Back →", history[-1])
#   history.pop(); print("Back →", history[-1])
#   print("Current:", history[-1])
#
# SOLUTION 6:
#   def rotate(lst, k):
#       k = k % len(lst)
#       return lst[k:] + lst[:k]
#   print(rotate([1,2,3,4,5], 2))
