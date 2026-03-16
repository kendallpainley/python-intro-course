"""
Module 16 Exercises: Modules & Packages
==========================================
"""
import math, random, datetime, json, os
print("=" * 55)
print("   Module 16 Exercises: Modules & Packages")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: math module
# Use the math module to compute:
#   a) area of a circle with radius 7
#   b) hypotenuse of a right triangle (legs 3 and 4)
#   c) 2^16 using math.pow  AND  using ** operator
#   d) log base 2 of 1024
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: math calculations


# ──────────────────────────────────────────────────────────
# Exercise 2: random module — Dice Simulator
# Simulate rolling two 6-sided dice 1000 times.
# Count how many times each sum (2-12) appears.
# Print the results as a bar chart using # characters.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: dice simulation and bar chart


# ──────────────────────────────────────────────────────────
# Exercise 3: datetime module
# Given a list of birthdays (as strings "YYYY-MM-DD"),
# calculate each person's age today and days until their
# next birthday. Print sorted by days until next birthday.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
people = [
    ("Alice",  "1990-03-15"),
    ("Bob",    "1985-11-28"),
    ("Carol",  "2000-07-04"),
    ("Dave",   "1978-01-20"),
]
# TODO: calculate ages and days until birthday


# ──────────────────────────────────────────────────────────
# Exercise 4: JSON round-trip
# Create a Python dict representing a config file with at
# least 5 settings of mixed types. Save to "config.json",
# read it back, modify one value, and save again.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
# TODO: JSON config round-trip


# ──────────────────────────────────────────────────────────
# Exercise 5 (Challenge): Create a utils module
# Create a file "my_utils.py" in the same directory with:
#   - clamp(value, min_v, max_v) → clamp value to range
#   - chunks(lst, size) → yield list in chunks of size
#   - flatten(nested) → flatten one level of nesting
# Import and test them here.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 — Challenge ]")
# TODO: create my_utils.py then import and test


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   print(math.pi * 7**2)            # circle area
#   print(math.hypot(3, 4))          # hypotenuse → 5.0
#   print(math.pow(2,16), 2**16)     # 65536.0 65536
#   print(math.log(1024, 2))         # 10.0
#
# SOLUTION 2:
#   counts = {n: 0 for n in range(2, 13)}
#   for _ in range(1000):
#       counts[random.randint(1,6) + random.randint(1,6)] += 1
#   for total, cnt in counts.items():
#       bar = "#" * (cnt // 10)
#       print(f"  {total:2}: {bar} ({cnt})")
#
# SOLUTION 3:
#   today = datetime.date.today()
#   result = []
#   for name, bday_str in people:
#       bday = datetime.datetime.strptime(bday_str, "%Y-%m-%d").date()
#       age = today.year - bday.year - ((today.month,today.day)<(bday.month,bday.day))
#       next_bday = bday.replace(year=today.year)
#       if next_bday < today: next_bday = next_bday.replace(year=today.year+1)
#       days = (next_bday - today).days
#       result.append((name, age, days))
#   for name, age, days in sorted(result, key=lambda x: x[2]):
#       print(f"  {name}: age {age}, {days} days until birthday")
#
# SOLUTION 4:
#   config = {"debug": True,"version":"1.0.0","max_retries":3,"timeout":30,"db_url":"sqlite:///app.db"}
#   with open("config.json","w") as f: json.dump(config,f,indent=2)
#   with open("config.json") as f: cfg = json.load(f)
#   cfg["debug"] = False
#   with open("config.json","w") as f: json.dump(cfg,f,indent=2)
#   print(cfg)
#
# SOLUTION 5 — my_utils.py content:
#   def clamp(v, lo, hi): return max(lo, min(hi, v))
#   def chunks(lst, n):
#       for i in range(0, len(lst), n): yield lst[i:i+n]
#   def flatten(nested): return [x for sub in nested for x in sub]
