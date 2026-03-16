"""
Module 18 Exercises: Iterators & Generators
=============================================
"""
print("=" * 55)
print("   Module 18 Exercises: Iterators & Generators")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Manual Iterator
# Build a class Range2 that behaves like range(start, stop, step)
# but is implemented from scratch using __iter__ and __next__.
# Test: list(Range2(0, 10, 2)) → [0, 2, 4, 6, 8]
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: Range2 class


# ──────────────────────────────────────────────────────────
# Exercise 2: Generator Pipeline
# Build a pipeline of 3 generators:
#   a) integers(start) — yields 1, 2, 3, 4, ... from start
#   b) squared(gen)    — yields each value squared from gen
#   c) take(gen, n)    — yields only the first n items
# Print the first 10 squared integers starting from 5.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: generator pipeline


# ──────────────────────────────────────────────────────────
# Exercise 3: Infinite Sequence
# Write a generator cycle(seq) that cycles through a sequence
# forever: cycle([1,2,3]) → 1,2,3,1,2,3,1,2,3,...
# Print the first 15 values of cycle(["A","B","C"]).
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
# TODO: cycle generator


# ──────────────────────────────────────────────────────────
# Exercise 4: Running Statistics
# Write a generator running_stats(data) that yields after
# each new number: (count, running_sum, running_average).
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
data = [4, 7, 13, 2, 1, 9, 3, 11]
# TODO: running_stats generator, iterate and print


# ──────────────────────────────────────────────────────────
# Exercise 5 (Challenge): Tree Traversal Generator
# Build a simple tree using dicts: {"val":1,"children":[...]}
# Write a generator depth_first(node) that traverses the tree
# depth-first and yields each node's value.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 — Challenge ]")
tree = {
    "val": 1,
    "children": [
        {"val": 2, "children": [
            {"val": 4, "children": []},
            {"val": 5, "children": []}
        ]},
        {"val": 3, "children": [
            {"val": 6, "children": []}
        ]}
    ]
}
# TODO: depth_first generator using yield from


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   class Range2:
#       def __init__(self,start,stop,step=1):
#           self.cur,self.stop,self.step=start,stop,step
#       def __iter__(self): return self
#       def __next__(self):
#           if (self.step>0 and self.cur>=self.stop) or (self.step<0 and self.cur<=self.stop):
#               raise StopIteration
#           val=self.cur; self.cur+=self.step; return val
#   print(list(Range2(0,10,2)))
#
# SOLUTION 2:
#   def integers(start=1):
#       n=start
#       while True: yield n; n+=1
#   def squared(gen):
#       for x in gen: yield x**2
#   def take(gen,n):
#       for _,x in zip(range(n),gen): yield x
#   print(list(take(squared(integers(5)),10)))
#
# SOLUTION 3:
#   def cycle(seq):
#       while True:
#           for item in seq: yield item
#   result=[next(cycle(["A","B","C"])) for _ in range(15)]
#   # Better:
#   gen=cycle(["A","B","C"])
#   print([next(gen) for _ in range(15)])
#
# SOLUTION 4:
#   def running_stats(data):
#       total=0
#       for i,x in enumerate(data,1):
#           total+=x
#           yield (i, total, total/i)
#   for count,s,avg in running_stats(data):
#       print(f"n={count} sum={s} avg={avg:.2f}")
#
# SOLUTION 5:
#   def depth_first(node):
#       yield node["val"]
#       for child in node["children"]:
#           yield from depth_first(child)
#   print(list(depth_first(tree)))  # [1,2,4,5,3,6]
