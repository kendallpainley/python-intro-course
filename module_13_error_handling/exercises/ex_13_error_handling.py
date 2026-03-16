"""
Module 13 Exercises: Error Handling & Exceptions
==================================================
"""
print("=" * 55)
print("   Module 13 Exercises: Error Handling")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Safe Conversion
# Write safe_int(value) that tries to convert value to int.
# Return the int on success, or None on failure.
# Test with: "42", "3.14", "hello", 99, True
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: safe_int function


# ──────────────────────────────────────────────────────────
# Exercise 2: Safe Division
# Write safe_divide(a, b) that returns a/b.
# Handle: ZeroDivisionError, TypeError (non-numeric inputs).
# Return None on error and print a descriptive message.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: safe_divide function


# ──────────────────────────────────────────────────────────
# Exercise 3: Robust Input Loop
# Ask the user to enter an integer between 1 and 10.
# Keep asking until they enter a valid value.
# Handle both ValueError (non-integer) and out-of-range.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
# TODO: input loop with error handling


# ──────────────────────────────────────────────────────────
# Exercise 4: Custom Exception
# Create a PasswordError exception.
# Write validate_password(pwd) that raises PasswordError if:
#   - shorter than 8 characters
#   - no uppercase letter
#   - no digit
# Test with several passwords.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
# TODO: PasswordError and validate_password


# ──────────────────────────────────────────────────────────
# Exercise 5 (Challenge): Retry Decorator Preview
# Write a function retry(func, times=3) that calls func().
# If func raises an exception, retry up to `times` attempts.
# If all fail, re-raise the last exception.
# Test by making a function that randomly fails.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 — Challenge ]")
import random
# TODO: retry function


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   def safe_int(value):
#       try: return int(value)
#       except (ValueError, TypeError): return None
#   for v in ["42","3.14","hello",99,True]: print(f"{v!r} → {safe_int(v)}")
#
# SOLUTION 2:
#   def safe_divide(a, b):
#       try: return a / b
#       except ZeroDivisionError: print("Cannot divide by zero"); return None
#       except TypeError as e: print(f"Type error: {e}"); return None
#   print(safe_divide(10,2), safe_divide(10,0), safe_divide("a",2))
#
# SOLUTION 3:
#   while True:
#       try:
#           n = int(input("Enter 1-10: "))
#           if 1 <= n <= 10: print(f"Got {n}"); break
#           else: print("Out of range!")
#       except ValueError: print("Not an integer!")
#
# SOLUTION 4:
#   class PasswordError(Exception): pass
#   def validate_password(pwd):
#       if len(pwd) < 8: raise PasswordError("Too short (min 8 chars)")
#       if not any(c.isupper() for c in pwd): raise PasswordError("Needs uppercase")
#       if not any(c.isdigit() for c in pwd): raise PasswordError("Needs a digit")
#       print(f"Password OK")
#   for p in ["short","allLower","NoDigit","Valid1Password"]:
#       try: validate_password(p)
#       except PasswordError as e: print(f"{p!r}: {e}")
#
# SOLUTION 5:
#   def retry(func, times=3):
#       last_error = None
#       for attempt in range(1, times+1):
#           try:
#               result = func()
#               print(f"Succeeded on attempt {attempt}")
#               return result
#           except Exception as e:
#               print(f"Attempt {attempt} failed: {e}")
#               last_error = e
#       raise last_error
#   def flaky():
#       if random.random() < 0.7: raise ValueError("Random failure!")
#       return "Success!"
#   try: print(retry(flaky, 5))
#   except ValueError: print("All attempts failed")
