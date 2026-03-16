"""
Module 06 Exercises: Control Flow
====================================
"""
print("=" * 55)
print("   Module 06 Exercises: Control Flow")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Number Sign
# Given num = -7, print whether it is "positive", "negative",
# or "zero" using if/elif/else.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
num = -7
# TODO: classify num


# ──────────────────────────────────────────────────────────
# Exercise 2: Grade Calculator
# Ask the user for a score (0-100) and print the letter grade:
#   90-100 → A, 80-89 → B, 70-79 → C, 60-69 → D, <60 → F
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: get score from input(), convert to int, print grade


# ──────────────────────────────────────────────────────────
# Exercise 3: Leap Year Checker
# A year is a leap year if:
#   divisible by 4 AND (not divisible by 100 OR divisible by 400)
# Ask for a year and print whether it is a leap year.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
# TODO: get year, apply the rule, print result


# ──────────────────────────────────────────────────────────
# Exercise 4: Ticket Pricing
# Movie ticket pricing rules:
#   age < 5:   free
#   age 5-12:  $8
#   age 13-64: $15
#   age 65+:   $10
# Get age from user, print the ticket price.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
# TODO: get age, determine price, print it


# ──────────────────────────────────────────────────────────
# Exercise 5: Ternary Rewrite
# Rewrite these if/else blocks as SINGLE-LINE ternary expressions:
#   a) if x > 0: label = "positive"  else: label = "non-positive"
#   b) if len(name) > 5: short = False  else: short = True
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 ]")
x = 10
name = "Ada"
# TODO: rewrite both as ternary expressions


# ──────────────────────────────────────────────────────────
# Exercise 6 (Challenge): Rock Paper Scissors (single round)
# Hardcode player1 = "rock" and player2 = "scissors"
# Determine and print the winner based on the rules.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 6 — Challenge ]")
player1 = "rock"
player2 = "scissors"
# TODO: determine winner using if/elif/else


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   if num > 0:
#       print("positive")
#   elif num < 0:
#       print("negative")
#   else:
#       print("zero")
#
# SOLUTION 2:
#   score = int(input("Score (0-100): "))
#   if score >= 90:   grade = "A"
#   elif score >= 80: grade = "B"
#   elif score >= 70: grade = "C"
#   elif score >= 60: grade = "D"
#   else:             grade = "F"
#   print(f"Grade: {grade}")
#
# SOLUTION 3:
#   year = int(input("Year: "))
#   is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#   print(f"{year} is {'a leap year' if is_leap else 'not a leap year'}")
#
# SOLUTION 4:
#   age = int(input("Age: "))
#   if age < 5:        price = 0
#   elif age <= 12:    price = 8
#   elif age <= 64:    price = 15
#   else:              price = 10
#   print(f"Ticket price: ${price}")
#
# SOLUTION 5:
#   label = "positive" if x > 0 else "non-positive"
#   short = True if len(name) <= 5 else False
#   print(label, short)
#
# SOLUTION 6:
#   beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
#   if player1 == player2:
#       print("It's a tie!")
#   elif beats[player1] == player2:
#       print(f"Player 1 wins! ({player1} beats {player2})")
#   else:
#       print(f"Player 2 wins! ({player2} beats {player1})")
