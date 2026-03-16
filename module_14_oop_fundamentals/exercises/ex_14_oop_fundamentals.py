"""
Module 14 Exercises: OOP Fundamentals
========================================
"""
print("=" * 55)
print("   Module 14 Exercises: OOP Fundamentals")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Student Class
# Create a Student class with:
#   - Attributes: name, student_id, grades (list)
#   - Method: add_grade(score) — append to grades
#   - Method: average() — return average grade
#   - Method: letter_grade() — return A/B/C/D/F
#   - __repr__ showing name, id, and average
# Test with at least 2 students.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: Student class


# ──────────────────────────────────────────────────────────
# Exercise 2: Rectangle Class
# Create a Rectangle class with:
#   - __init__(width, height) — validate both > 0
#   - Properties: area, perimeter
#   - Method: is_square() → bool
#   - Method: scale(factor) → new Rectangle (scaled)
#   - __repr__
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: Rectangle class


# ──────────────────────────────────────────────────────────
# Exercise 3: Class Method Constructor
# Build a Person class.
# Add a @classmethod from_birth_year(cls, name, birth_year)
# that creates a Person calculating age from 2024.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
# TODO: Person class with from_birth_year classmethod


# ──────────────────────────────────────────────────────────
# Exercise 4 (Challenge): Todo List Class
# Build a TodoList class with:
#   - add(task)      — add a task
#   - complete(task) — mark task as done
#   - remove(task)   — remove a task
#   - pending()      — return list of incomplete tasks
#   - done()         — return list of completed tasks
#   - __repr__       — show counts
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 — Challenge ]")
# TODO: TodoList class


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   class Student:
#       def __init__(self, name, student_id):
#           self.name, self.student_id, self.grades = name, student_id, []
#       def add_grade(self, score): self.grades.append(score)
#       def average(self): return sum(self.grades)/len(self.grades) if self.grades else 0
#       def letter_grade(self):
#           avg = self.average()
#           if avg>=90: return "A"
#           elif avg>=80: return "B"
#           elif avg>=70: return "C"
#           elif avg>=60: return "D"
#           return "F"
#       def __repr__(self): return f"Student({self.name!r}, avg={self.average():.1f}, {self.letter_grade()})"
#   s1 = Student("Alice","S001"); s1.add_grade(90); s1.add_grade(85)
#   print(s1)
#
# SOLUTION 2:
#   class Rectangle:
#       def __init__(self,w,h):
#           if w<=0 or h<=0: raise ValueError("Dimensions must be positive")
#           self.width, self.height = w, h
#       @property
#       def area(self): return self.width * self.height
#       @property
#       def perimeter(self): return 2*(self.width+self.height)
#       def is_square(self): return self.width == self.height
#       def scale(self, f): return Rectangle(self.width*f, self.height*f)
#       def __repr__(self): return f"Rectangle({self.width}x{self.height})"
#   r = Rectangle(4,3); print(r, r.area, r.perimeter, r.is_square())
#   print(r.scale(2))
#
# SOLUTION 3:
#   class Person:
#       def __init__(self, name, age):
#           self.name, self.age = name, age
#       @classmethod
#       def from_birth_year(cls, name, birth_year):
#           return cls(name, 2024-birth_year)
#       def __repr__(self): return f"Person({self.name!r}, age={self.age})"
#   p = Person.from_birth_year("Alice", 1994); print(p)
#
# SOLUTION 4:
#   class TodoList:
#       def __init__(self): self._tasks = {}
#       def add(self, task): self._tasks[task] = False
#       def complete(self, task):
#           if task in self._tasks: self._tasks[task] = True
#       def remove(self, task): self._tasks.pop(task, None)
#       def pending(self): return [t for t,d in self._tasks.items() if not d]
#       def done(self): return [t for t,d in self._tasks.items() if d]
#       def __repr__(self): return f"TodoList(pending={len(self.pending())}, done={len(self.done())})"
#   tl = TodoList()
#   for t in ["Buy milk","Write code","Exercise"]: tl.add(t)
#   tl.complete("Write code")
#   print(tl); print("Pending:", tl.pending()); print("Done:", tl.done())
