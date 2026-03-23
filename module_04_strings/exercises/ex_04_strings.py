"""
Module 04 Exercises: Strings In Depth
=======================================
"""
print("=" * 55)
print("   Module 04 Exercises: Strings")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Indexing & Length
# Given the string below, print:
#   - the first character, last character, and middle character
#   - the total length
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
word = "programming"

mid = len(word) // 2
print(word[0], word[-1], word[mid], len(word))


# ──────────────────────────────────────────────────────────
# Exercise 2: Slicing Practice
# From the string "Hello, World!", extract and print:
#   a) "Hello"   b) "World"   c) the last 6 characters
#   d) every other character   e) the string reversed
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
s = "Hello, World!"

print(len(s))
print(s[:5], s[7:12], s[6:], s[0::2], s[::-1], sep=" --- ")


# ──────────────────────────────────────────────────────────
# Exercise 3: Method Chain
# Given the messy string below:
#   a) Strip whitespace
#   b) Convert to title case
#   c) Replace "Pythn" with "Python"
# Print the cleaned result.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
messy = "  learning pythn is fun!  "

print(messy.strip().title().replace("Pythn", "Python"))


# ──────────────────────────────────────────────────────────
# Exercise 4: f-String Formatting
# Create a formatted receipt:
#   Item: Widget
#   Price: $19.99
#   Quantity: 3
#   Total: $59.97
# Use f-strings with formatting specifiers for the prices.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
item = "Widget"
price = 19.99
quantity = 3

print(f'Item: {item} \nPrice: {price} \nQuantity: {quantity} \nTotal: {price * quantity}')


# ──────────────────────────────────────────────────────────
# Exercise 5: Word Counter
# Count how many words are in the sentence below.
# Then print each word on its own line (numbered).
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 ]")
sentence = "The quick brown fox jumps over the lazy dog"

count = len(sentence.split())




# ──────────────────────────────────────────────────────────
# Exercise 6: Palindrome Checker
# Check if the string "racecar" is the same forwards and backwards.
# Print: "'racecar' is a palindrome: True/False"
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 6 ]")
test_word = "racecar"

if test_word[::-1] == test_word:
    print(f"'racecar' is a palindrome: True")
else:
    print(f"'racecar' is a palindrome: False")


# ──────────────────────────────────────────────────────────
# Exercise 7 (Challenge): Caesar Cipher
# Shift each letter in "hello" forward by 3 positions (a→d, b→e...)
# Hint: use ord() to get ASCII value, chr() to convert back
# ord("a") = 97, chr(97) = "a"
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 7 — Challenge ]")
plaintext = "hello"




print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   mid = len(word) // 2
#   print(f"First: {word[0]}, Last: {word[-1]}, Middle: {word[mid]}")
#   print(f"Length: {len(word)}")
#
# SOLUTION 2:
#   print(s[:5])          # Hello
#   print(s[7:12])        # World
#   print(s[-6:])         # World!
#   print(s[::2])         # Hlo ol!
#   print(s[::-1])        # !dlroW ,olleH
#
# SOLUTION 3:
#   cleaned = messy.strip().title().replace("Pythn", "Python")
#   print(cleaned)
#
# SOLUTION 4:
#   total = price * quantity
#   print(f"Item:     {item}")
#   print(f"Price:    ${price:.2f}")
#   print(f"Quantity: {quantity}")
#   print(f"Total:    ${total:.2f}")
#
# SOLUTION 5:
#   words = sentence.split()
#   print(f"Word count: {len(words)}")
#   for i, w in enumerate(words, 1):
#       print(f"  {i}. {w}")
#
# SOLUTION 6:
#   is_palindrome = test_word == test_word[::-1]
#   print(f"'{test_word}' is a palindrome: {is_palindrome}")
#
# SOLUTION 7:
#   result = ""
#   for ch in plaintext:
#       result += chr(ord(ch) + 3)
#   print(f"Encrypted: {result}")   # khoor
