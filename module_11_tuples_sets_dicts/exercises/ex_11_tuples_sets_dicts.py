"""
Module 11 Exercises: Tuples, Sets & Dictionaries
==================================================
"""
print("=" * 55)
print("   Module 11 Exercises: Tuples, Sets & Dicts")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Tuple Unpacking
# Swap using tuple unpacking:
# a, b, c = 1, 2, 3  →  c, b, a (all three swapped)
# Then unpack (10, 20, 30, 40, 50) into first, second, *rest
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: tuple swap and extended unpacking


# ──────────────────────────────────────────────────────────
# Exercise 2: Set Operations
# words1 = words in sentence 1, words2 = words in sentence 2
# Print: words in both, only in 1, only in 2, in either but not both
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
sentence1 = "the quick brown fox jumps over the lazy dog"
sentence2 = "the fox ran quickly over the hill in the morning"
words1 = set(sentence1.split())
words2 = set(sentence2.split())
# TODO: intersection, difference (both), symmetric difference


# ──────────────────────────────────────────────────────────
# Exercise 3: Word Frequency Counter
# Count how many times each word appears in the text.
# Use a dict. Print the 3 most common words.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
text = "to be or not to be that is the question to be is to act"
# TODO: count word frequencies in a dict, print top 3


# ──────────────────────────────────────────────────────────
# Exercise 4: Phonebook
# Create a dict mapping names to phone numbers.
# Add, update, and look up entries.
# Print all entries neatly formatted.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
# TODO: build and manipulate a phonebook dict


# ──────────────────────────────────────────────────────────
# Exercise 5: Grade Book
# Given the nested dict of students, compute each student's
# average score and print a sorted report (highest avg first).
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 ]")
gradebook = {
    "Alice": [88, 92, 79, 95],
    "Bob":   [72, 68, 75, 80],
    "Carol": [95, 98, 91, 99],
    "Dave":  [60, 55, 70, 65],
}
# TODO: compute averages, sort by average desc, print report


# ──────────────────────────────────────────────────────────
# Exercise 6 (Challenge): Invert a Dictionary
# Given {a:1, b:2, c:3}, produce {1:a, 2:b, 3:c}
# Handle the case where multiple keys share the same value
# (store them in a list).
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 6 — Challenge ]")
original = {"a": 1, "b": 2, "c": 1, "d": 3}
# TODO: invert the dict


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   a, b, c = 1, 2, 3
#   a, b, c = c, b, a
#   print(a, b, c)  # 3 2 1
#   first, second, *rest = (10, 20, 30, 40, 50)
#   print(first, second, rest)
#
# SOLUTION 2:
#   print("Both:   ", words1 & words2)
#   print("Only 1: ", words1 - words2)
#   print("Only 2: ", words2 - words1)
#   print("Sym diff:", words1 ^ words2)
#
# SOLUTION 3:
#   freq = {}
#   for word in text.split():
#       freq[word] = freq.get(word, 0) + 1
#   top3 = sorted(freq, key=lambda w: freq[w], reverse=True)[:3]
#   for w in top3: print(f"  {w!r}: {freq[w]}")
#
# SOLUTION 4:
#   phones = {"Alice": "555-0101", "Bob": "555-0102"}
#   phones["Carol"] = "555-0103"
#   phones["Alice"] = "555-9999"
#   print(phones.get("Bob", "not found"))
#   for name, num in phones.items(): print(f"  {name}: {num}")
#
# SOLUTION 5:
#   avgs = {name: sum(scores)/len(scores) for name, scores in gradebook.items()}
#   for name, avg in sorted(avgs.items(), key=lambda x: x[1], reverse=True):
#       print(f"  {name:8} avg: {avg:.1f}")
#
# SOLUTION 6:
#   inverted = {}
#   for k, v in original.items():
#       inverted.setdefault(v, []).append(k)
#   print(inverted)
