"""
Module 15 Exercises: Advanced OOP
=====================================
"""
print("=" * 55)
print("   Module 15 Exercises: Advanced OOP")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Shape Hierarchy
# Create: Shape (base) → Circle, Rectangle, Triangle
# Each must implement:
#   - area() and perimeter()
#   - __repr__ showing type and dimensions
# Create a list of mixed shapes, print area of each.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
import math
# TODO: Shape hierarchy


# ──────────────────────────────────────────────────────────
# Exercise 2: Employee Hierarchy
# Employee (base): name, salary, work()
# Manager(Employee): team (list), add_to_team(), work() override
# Engineer(Employee): specialty, work() override
# Create each, call work() on all via a loop.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: Employee hierarchy


# ──────────────────────────────────────────────────────────
# Exercise 3: Fraction Class with Dunder Methods
# Build a Fraction class (numerator, denominator) with:
#   __add__, __sub__, __mul__, __truediv__
#   __eq__, __lt__, __gt__
#   __repr__ showing "3/4"
#   Automatically reduce to lowest terms using gcd.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
from math import gcd
# TODO: Fraction class


# ──────────────────────────────────────────────────────────
# Exercise 4 (Challenge): Mixin Classes
# Create mixins: JsonMixin (to_json()), LogMixin (log(msg))
# Apply them to a Product class.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 — Challenge ]")
import json
# TODO: mixins + Product class


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   class Shape:
#       def area(self): raise NotImplementedError
#       def perimeter(self): raise NotImplementedError
#   class Circle(Shape):
#       def __init__(self,r): self.r = r
#       def area(self): return math.pi*self.r**2
#       def perimeter(self): return 2*math.pi*self.r
#       def __repr__(self): return f"Circle(r={self.r})"
#   class Rectangle(Shape):
#       def __init__(self,w,h): self.w,self.h=w,h
#       def area(self): return self.w*self.h
#       def perimeter(self): return 2*(self.w+self.h)
#       def __repr__(self): return f"Rectangle({self.w}x{self.h})"
#   shapes=[Circle(5),Rectangle(4,6)]
#   for s in shapes: print(f"{s}: area={s.area():.2f}")
#
# SOLUTION 2:
#   class Employee:
#       def __init__(self,name,salary): self.name,self.salary=name,salary
#       def work(self): return f"{self.name} is working"
#   class Manager(Employee):
#       def __init__(self,name,salary): super().__init__(name,salary); self.team=[]
#       def add_to_team(self,emp): self.team.append(emp)
#       def work(self): return f"{self.name} manages {len(self.team)} people"
#   class Engineer(Employee):
#       def __init__(self,name,salary,spec): super().__init__(name,salary); self.spec=spec
#       def work(self): return f"{self.name} engineers {self.spec}"
#   m=Manager("Alice",80000); e=Engineer("Bob",70000,"backend"); m.add_to_team(e)
#   for emp in [m,e]: print(emp.work())
#
# SOLUTION 3:
#   class Fraction:
#       def __init__(self,n,d):
#           g=gcd(abs(n),abs(d)); self.n,self.d=n//g,d//g
#       def __repr__(self): return f"{self.n}/{self.d}"
#       def __add__(self,o): return Fraction(self.n*o.d+o.n*self.d,self.d*o.d)
#       def __sub__(self,o): return Fraction(self.n*o.d-o.n*self.d,self.d*o.d)
#       def __mul__(self,o): return Fraction(self.n*o.n,self.d*o.d)
#       def __truediv__(self,o): return Fraction(self.n*o.d,self.d*o.n)
#       def __eq__(self,o): return self.n==o.n and self.d==o.d
#       def __lt__(self,o): return self.n*o.d < o.n*self.d
#   a,b=Fraction(1,2),Fraction(1,3); print(a+b,a-b,a*b,a/b)
#
# SOLUTION 4:
#   class JsonMixin:
#       def to_json(self): return json.dumps(self.__dict__)
#   class LogMixin:
#       def log(self,msg): print(f"[LOG] {type(self).__name__}: {msg}")
#   class Product(JsonMixin, LogMixin):
#       def __init__(self,name,price): self.name,self.price=name,price
#   p=Product("Widget",9.99); print(p.to_json()); p.log("created")
