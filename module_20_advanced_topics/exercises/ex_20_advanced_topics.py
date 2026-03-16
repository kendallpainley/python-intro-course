"""
Module 20 Exercises: Advanced Python
========================================
"""
print("=" * 55)
print("   Module 20 Exercises: Advanced Python")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Type-Annotated Data Pipeline
# Write a fully type-annotated function pipeline:
#   parse_csv(text: str) -> list[dict[str, str]]
#   compute_stats(records: list[dict], field: str) -> dict[str, float]
#     (returns min, max, avg of numeric field)
# Annotate everything including return types.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: type-annotated pipeline


# ──────────────────────────────────────────────────────────
# Exercise 2: Dataclass Inventory System
# Create a Product dataclass (name, price, quantity).
# Create an Inventory dataclass that holds a list of Products.
# Add methods: add_product, total_value, find_by_name,
#              most_expensive, out_of_stock (quantity=0)
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
from dataclasses import dataclass, field
# TODO: Product and Inventory dataclasses


# ──────────────────────────────────────────────────────────
# Exercise 3: collections Challenge
# Given a string of text, use Counter to:
#   a) Find the 5 most common letters (ignore spaces/punct)
#   b) Find letters that appear exactly once
# Use defaultdict to build an index: {letter: [positions]}
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
from collections import Counter, defaultdict
import string
text = "the quick brown fox jumps over the lazy dog"
# TODO: Counter analysis and defaultdict index


# ──────────────────────────────────────────────────────────
# Exercise 4: itertools Pipeline
# Given a list of sales records (date, product, amount),
# use itertools.groupby to group by product and print:
#   Product: X → total: $Y.YY across N sales
# (Sort by product before groupby!)
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
import itertools
sales = [
    ("2024-01", "Widget", 99.99),
    ("2024-01", "Gadget", 149.99),
    ("2024-02", "Widget", 89.99),
    ("2024-02", "Widget", 99.99),
    ("2024-03", "Gadget", 159.99),
    ("2024-03", "Doohickey", 29.99),
]
# TODO: groupby product, sum amounts


# ──────────────────────────────────────────────────────────
# Exercise 5 (Challenge): Mini Test Suite
# Write pytest-style tests (as regular functions) for a
# Stack class you implement here.
# Stack must have: push, pop, peek, is_empty, __len__
# Write at least 8 tests. Run them with a simple test runner.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 — Challenge ]")
# TODO: Stack class + test functions + runner


print("\n" + "=" * 55)
print("\n🎉 Congratulations on reaching Module 20!")
print("You have covered Python from fundamentals to advanced.")
print("Keep building, keep learning!")
print("=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   def parse_csv(text: str) -> list[dict[str, str]]:
#       lines = text.strip().split("\n")
#       headers = lines[0].split(",")
#       return [{h: v for h,v in zip(headers, line.split(","))} for line in lines[1:]]
#   def compute_stats(records: list[dict], field: str) -> dict[str, float]:
#       vals = [float(r[field]) for r in records]
#       return {"min":min(vals),"max":max(vals),"avg":sum(vals)/len(vals)}
#
# SOLUTION 2:
#   @dataclass
#   class Product:
#       name: str; price: float; quantity: int
#   @dataclass
#   class Inventory:
#       products: list = field(default_factory=list)
#       def add_product(self,p): self.products.append(p)
#       def total_value(self): return sum(p.price*p.quantity for p in self.products)
#       def find_by_name(self,n): return next((p for p in self.products if p.name==n),None)
#       def most_expensive(self): return max(self.products,key=lambda p:p.price)
#       def out_of_stock(self): return [p for p in self.products if p.quantity==0]
#
# SOLUTION 3:
#   letters = [c for c in text.lower() if c in string.ascii_lowercase]
#   c = Counter(letters)
#   print(c.most_common(5))
#   print([l for l,n in c.items() if n==1])
#   idx = defaultdict(list)
#   for i,ch in enumerate(text.lower()):
#       if ch in string.ascii_lowercase: idx[ch].append(i)
#   print(dict(idx))
#
# SOLUTION 4:
#   sorted_sales = sorted(sales, key=lambda r: r[1])
#   for product, group in itertools.groupby(sorted_sales, key=lambda r: r[1]):
#       items = list(group)
#       total = sum(r[2] for r in items)
#       print(f"  {product}: ${total:.2f} across {len(items)} sales")
#
# SOLUTION 5:
#   class Stack:
#       def __init__(self): self._data=[]
#       def push(self,x): self._data.append(x)
#       def pop(self):
#           if self.is_empty(): raise IndexError("pop from empty stack")
#           return self._data.pop()
#       def peek(self):
#           if self.is_empty(): raise IndexError("peek from empty stack")
#           return self._data[-1]
#       def is_empty(self): return len(self._data)==0
#       def __len__(self): return len(self._data)
#   def run_tests():
#       passed=0; failed=0
#       def test(name, expr):
#           nonlocal passed,failed
#           try: assert expr; print(f"  ✓ {name}"); passed+=1
#           except AssertionError: print(f"  ✗ {name}"); failed+=1
#       s=Stack()
#       test("empty stack is_empty", s.is_empty())
#       test("empty stack len=0", len(s)==0)
#       s.push(1); s.push(2); s.push(3)
#       test("push/len=3", len(s)==3)
#       test("peek=3", s.peek()==3)
#       test("pop=3", s.pop()==3)
#       test("after pop len=2", len(s)==2)
#       test("not empty", not s.is_empty())
#       print(f"\n  {passed} passed, {failed} failed")
#   run_tests()
