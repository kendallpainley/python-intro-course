"""
Module 12 Exercises: File I/O
================================
"""
import csv
from pathlib import Path

print("=" * 55)
print("   Module 12 Exercises: File I/O")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Write and Read
# Create a file "poem.txt" with at least 5 lines.
# Read it back and print each line numbered.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: write poem.txt then read and number each line


# ──────────────────────────────────────────────────────────
# Exercise 2: Word Count
# Write a function word_count(filename) that returns:
# {total_lines, total_words, total_chars} for a text file.
# Test it on poem.txt from Exercise 1.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: word_count function, test on poem.txt


# ──────────────────────────────────────────────────────────
# Exercise 3: Log File Builder
# Append 5 timestamped log entries to "app.log".
# Format: "2024-01-15 10:30:00 | INFO | Message here"
# Then read and print all entries.
# Use datetime.datetime.now() for the timestamp.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
import datetime
# TODO: append log entries, read them back


# ──────────────────────────────────────────────────────────
# Exercise 4: CSV Grade Reporter
# Write a CSV with columns: Name, Math, Science, English
# Include 4 students with scores.
# Read it back and compute each student's average.
# Print a report sorted by average (highest first).
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
# TODO: write grades CSV, read back, compute averages, print report


# ──────────────────────────────────────────────────────────
# Exercise 5 (Challenge): Find and Replace
# Read "poem.txt", replace a specific word with another,
# and write the result to "poem_edited.txt".
# Print both original and edited versions side by side.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 — Challenge ]")
# TODO: read, replace word, write to new file, compare


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   poem = ["Roses are red\n","Violets are blue\n","Python is great\n","And so are you\n","Keep coding on!\n"]
#   with open("poem.txt","w") as f: f.writelines(poem)
#   with open("poem.txt") as f:
#       for i,line in enumerate(f,1): print(f"{i}: {line.strip()}")
#
# SOLUTION 2:
#   def word_count(filename):
#       with open(filename) as f:
#           lines = f.readlines()
#       words = sum(len(l.split()) for l in lines)
#       chars = sum(len(l) for l in lines)
#       return {"lines": len(lines), "words": words, "chars": chars}
#   print(word_count("poem.txt"))
#
# SOLUTION 3:
#   messages = ["Server started","Request received","DB query OK","Response sent","Server running"]
#   with open("app.log","a") as f:
#       for msg in messages:
#           ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#           f.write(f"{ts} | INFO | {msg}\n")
#   with open("app.log") as f: print(f.read())
#
# SOLUTION 4:
#   rows = [["Name","Math","Science","English"],["Alice",90,88,92],["Bob",75,80,70],["Carol",95,92,98],["Dave",60,65,55]]
#   with open("grades.csv","w",newline="") as f: csv.writer(f).writerows(rows)
#   with open("grades.csv") as f:
#       for row in csv.DictReader(f):
#           avg = (int(row["Math"])+int(row["Science"])+int(row["English"]))/3
#           print(f"{row['Name']}: {avg:.1f}")
#
# SOLUTION 5:
#   original = Path("poem.txt").read_text()
#   edited = original.replace("red", "crimson")
#   Path("poem_edited.txt").write_text(edited)
#   print("Original:"); print(original)
#   print("Edited:"); print(edited)
