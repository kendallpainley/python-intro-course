"""
Module 19 Exercises: Decorators & Closures
============================================
"""
from functools import wraps
import time

print("=" * 55)
print("   Module 19 Exercises: Decorators & Closures")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# Exercise 1: Memoization Closure
# Build make_memoized(func) — a closure that caches results.
# Results are stored in a dict inside the closure.
# Test with an expensive function like slow_square(n) that
# has a time.sleep(0.1) inside.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 1 ]")
# TODO: make_memoized closure


# ──────────────────────────────────────────────────────────
# Exercise 2: @validate_types decorator
# Write a decorator validate_args that checks:
#   - All arguments must be numeric (int or float)
#   - Raise TypeError with a helpful message if not
# Apply it to an add(a, b) function.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 2 ]")
# TODO: validate_args decorator


# ──────────────────────────────────────────────────────────
# Exercise 3: Rate Limiter
# Write a @rate_limit(calls_per_second) decorator that
# ensures a function is called at most N times per second.
# If called too fast, sleep to enforce the limit.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 3 ]")
# TODO: rate_limit decorator factory


# ──────────────────────────────────────────────────────────
# Exercise 4: Debug Decorator
# Write @debug that prints:
#   → calling func_name(args, kwargs)
#   ← func_name returned <result> in Xms
# Apply it to several functions and test.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 4 ]")
# TODO: debug decorator


# ──────────────────────────────────────────────────────────
# Exercise 5 (Challenge): Class-based Decorator
# Implement the @timer decorator as a CLASS (not a function).
# Use __call__ to make instances callable.
# ──────────────────────────────────────────────────────────
print("\n[ Exercise 5 — Challenge ]")
# TODO: class-based Timer decorator


print("\n" + "=" * 55)


# ╔══════════════════════════════════════════════════════════╗
# ║            !! SOLUTIONS BELOW — TRY FIRST !!            ║
# ╚══════════════════════════════════════════════════════════╝
#
# SOLUTION 1:
#   def make_memoized(func):
#       cache = {}
#       def wrapper(*args):
#           if args not in cache:
#               cache[args] = func(*args)
#           return cache[args]
#       return wrapper
#   def slow_square(n): time.sleep(0.01); return n**2
#   m = make_memoized(slow_square)
#   t=time.time(); m(5); m(5); m(5); print(f"Took {time.time()-t:.3f}s (cached)")
#
# SOLUTION 2:
#   def validate_args(func):
#       @wraps(func)
#       def wrapper(*args, **kwargs):
#           for a in list(args)+list(kwargs.values()):
#               if not isinstance(a,(int,float)):
#                   raise TypeError(f"Expected numeric, got {type(a).__name__}")
#           return func(*args, **kwargs)
#       return wrapper
#   @validate_args
#   def add(a,b): return a+b
#   print(add(3,4))
#   try: add("x",4)
#   except TypeError as e: print(e)
#
# SOLUTION 3:
#   def rate_limit(calls_per_second):
#       min_interval = 1.0 / calls_per_second
#       def decorator(func):
#           last_called = [0.0]
#           @wraps(func)
#           def wrapper(*args,**kwargs):
#               elapsed = time.time()-last_called[0]
#               if elapsed < min_interval: time.sleep(min_interval-elapsed)
#               last_called[0]=time.time()
#               return func(*args,**kwargs)
#           return wrapper
#       return decorator
#
# SOLUTION 4:
#   def debug(func):
#       @wraps(func)
#       def wrapper(*args,**kwargs):
#           print(f"→ calling {func.__name__}({args}, {kwargs})")
#           t=time.perf_counter(); result=func(*args,**kwargs)
#           print(f"← {func.__name__} returned {result!r} in {(time.perf_counter()-t)*1000:.2f}ms")
#           return result
#       return wrapper
#   @debug
#   def multiply(a,b): return a*b
#   multiply(3,7)
#
# SOLUTION 5:
#   class Timer:
#       def __init__(self,func): wraps(func)(self); self.func=func
#       def __call__(self,*args,**kwargs):
#           t=time.perf_counter(); r=self.func(*args,**kwargs)
#           print(f"{self.func.__name__} took {time.perf_counter()-t:.6f}s"); return r
#   @Timer
#   def my_func(n): return sum(range(n))
#   my_func(100000)
