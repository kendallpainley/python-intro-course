"""
Module 07 Exercises: While Loops
===================================
"""
print("=" * 55)
print("   Module 07 Exercises: While Loops")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Countdown
# Print a countdown from 10 to 1, then print "Liftoff!"
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: while loop countdown from 10 to 1, then "Liftoff!"


# ──────────────────────────────────────────────────────────
# Exercise 2: Sum Until Quit
# Repeatedly ask the user to enter a number.
# Keep a running total. When they type "done", print the total.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: accumulate a sum until user types "done"


# ──────────────────────────────────────────────────────────
# Exercise 3: Guess the Number
# The secret number is 42.
# Keep asking the user to guess until they get it right.
# After each wrong guess, say "Too high" or "Too low".
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
secret = 42
# TODO: guessing game loop


# ──────────────────────────────────────────────────────────
# Exercise 4: FizzBuzz with While
# Print numbers 1-30. But:
#   divisible by 3 → print "Fizz"
#   divisible by 5 → print "Buzz"
#   divisible by both → print "FizzBuzz"
#   otherwise → print the number
# Use a while loop.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
# TODO: FizzBuzz 1-30 with while loop


# ──────────────────────────────────────────────────────────
# Exercise 5 (Challenge): Collatz Conjecture
# Start with any positive integer n.
# If n is even: n = n / 2
# If n is odd:  n = 3n + 1
# Repeat until n == 1. Count the steps.
# Try starting with n = 27 — it takes 111 steps!
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 — Challenge ]")
n = 27
# TODO: count steps to reach 1 via Collatz sequence


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   n = 10
#   while n >= 1:
#       print(n)
#       n -= 1
#   print("Liftoff!")
#
# SOLUTION 2:
#   total = 0
#   while True:
#       entry = input("Enter a number (or 'done'): ")
#       if entry == "done":
#           break
#       total += float(entry)
#   print(f"Total: {total}")
#
# SOLUTION 3:
#   while True:
#       guess = int(input("Guess the number: "))
#       if guess == secret:
#           print("Correct!")
#           break
#       elif guess > secret:
#           print("Too high!")
#       else:
#           print("Too low!")
#
# SOLUTION 4:
#   n = 1
#   while n <= 30:
#       if n % 15 == 0:   print("FizzBuzz")
#       elif n % 3 == 0:  print("Fizz")
#       elif n % 5 == 0:  print("Buzz")
#       else:             print(n)
#       n += 1
#
# SOLUTION 5:
#   steps = 0
#   start = n
#   while n != 1:
#       if n % 2 == 0:
#           n = n // 2
#       else:
#           n = 3 * n + 1
#       steps += 1
#   print(f"Starting from {start}: reached 1 in {steps} steps")
