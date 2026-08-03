"""
Functions and Modules - Intermediate Python Lesson 3
======================================================

This lesson covers advanced function concepts and module usage.

Topics Covered:
1. Advanced Function Arguments (*args, **kwargs)
2. Lambda Functions
3. Decorators
4. Generators and yield
5. Recursion
6. Import System and Creating Modules
7. Built-in Functions Deep Dive
"""

# ============================================
# 1. ADVANCED FUNCTION ARGUMENTS
# ============================================

print("=" * 50)
print("ADVANCED FUNCTION ARGUMENTS")
print("=" * 50)

# Positional and keyword arguments
def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

print(greet("Alice", "Smith"))
print(greet(last_name="Smith", first_name="Alice"))

# Default arguments
def power(base, exponent=2):
    return base ** exponent

print(f"2^2 = {power(2)}")
print(f"2^3 = {power(2, 3)}")

# *args - Variable positional arguments
def sum_all(*args):
    """Accept any number of positional arguments"""
    return sum(args)

print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")
print(f"Sum: {sum_all(10, 20, 30)}")

# **kwargs - Variable keyword arguments
def print_info(**kwargs):
    """Accept any number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nPerson Info:")
print_info(name="Alice", age=25, city="New York")

# Combining all argument types
def complete_example(pos1, pos2, *args, default="default", **kwargs):
    print(f"Positional: {pos1}, {pos2}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

complete_example("a", "b", 1, 2, 3, name="Test", value=100)


# ============================================
# 2. LAMBDA FUNCTIONS
# ============================================

print("\n" + "=" * 50)
print("LAMBDA FUNCTIONS")
print("=" * 50)

# Basic lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

# Lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# Lambda with sorted()
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_by_second = sorted(pairs, key=lambda x: x[1])
print(f"Sorted by second element: {sorted_by_second}")

# Practical: Sort students by grade
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
print(f"\nTop student: {sorted_students[0]['name']} ({sorted_students[0]['grade']})")


# ============================================
# 3. DECORATORS
# ============================================

print("\n" + "=" * 50)
print("DECORATORS")
print("=" * 50)

# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet_person(name):
    print(f"Hello, {name}!")

print("\nGreeting 3 times:")
greet_person("Alice")

# Practical: Timing decorator
import time
from functools import wraps

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)
    return "Done"

print("\nTiming example:")
slow_function()

# Practical: Logging decorator
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def multiply(a, b):
    return a * b

print("\nLogging example:")
multiply(5, 3)


# ============================================
# 4. GENERATORS AND YIELD
# ============================================

print("\n" + "=" * 50)
print("GENERATORS AND YIELD")
print("=" * 50)

# Generator function
def countdown(n):
    """Generate numbers from n down to 0"""
    while n >= 0:
        yield n
        n -= 1

print("Countdown from 5:")
for num in countdown(5):
    print(num, end=" ")
print()

# Generator expression
squares_gen = (x**2 for x in range(5))
print(f"\nSquares generator: {list(squares_gen)}")

# Memory efficient example
def fibonacci_generator(n):
    """Generate Fibonacci sequence"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(f"\nFibonacci (first 10): {list(fibonacci_generator(10))}")

# Infinite generator
def infinite_counter():
    """Count infinitely"""
    count = 0
    while True:
        yield count
        count += 1

# Use with next() or break
counter = infinite_counter()
print(f"\nInfinite counter: {[next(counter) for _ in range(5)]}")


# ============================================
# 5. RECURSION
# ============================================

print("\n" + "=" * 50)
print("RECURSION")
print("=" * 50)

# Factorial using recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")

# Fibonacci using recursion
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

print(f"Fibonacci(10) = {fib_recursive(10)}")

# Recursive sum of list
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(f"Sum [1,2,3,4,5] = {sum_list([1, 2, 3, 4, 5])}")

# Tower of Hanoi
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)

print("\nTower of Hanoi (3 disks):")
hanoi(3, 'A', 'C', 'B')


# ============================================
# 6. IMPORT SYSTEM AND CREATING MODULES
# ============================================

print("\n" + "=" * 50)
print("IMPORT SYSTEM AND CREATING MODULES")
print("=" * 50)

# Different import methods
import math
from math import sqrt, pi
from math import *  # Not recommended

print(f"sqrt(16) = {sqrt(16)}")
print(f"pi = {pi:.4f}")

# Import with alias
import numpy as np  # Common convention
import pandas as pd

# Create your own module (example structure)
"""
# Save this as mymodule.py:

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159

# Then import:
# import mymodule
# from mymodule import greet, add
"""

# Check module location
print(f"\nmath module location: {math.__file__}")

# List available modules
import sys
print(f"\nPython path: {sys.path[:3]}...")  # First 3 paths


# ============================================
# 7. BUILT-IN FUNCTIONS DEEP DIVE
# ============================================

print("\n" + "=" * 50)
print("BUILT-IN FUNCTIONS DEEP DIVE")
print("=" * 50)

# enumerate() - Get index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# zip() - Combine iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# any() and all()
numbers = [1, 0, 3, 4]
print(f"\nany([1,0,3,4]) = {any(numbers)}")  # True if any truthy
print(f"all([1,0,3,4]) = {all(numbers)}")   # True if all truthy

# isinstance() and type()
x = 5
print(f"\nisinstance(5, int) = {isinstance(x, int)}")
print(f"type(5) = {type(x)}")

# getattr(), setattr(), delattr()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(f"\ngetattr(p, 'name') = {getattr(p, 'name')}")
setattr(p, 'age', 26)
print(f"After setattr: p.age = {p.age}")

# dir() - List attributes
print(f"\nPerson attributes: {dir(p)[:5]}...")  # First 5

# help() - Get documentation
# help(str)  # Uncomment to see string documentation

# Practical: Custom zip implementation
def custom_zip(list1, list2):
    result = []
    for i in range(min(len(list1), len(list2))):
        result.append((list1[i], list2[i]))
    return result

print(f"\nCustom zip: {custom_zip([1,2,3], ['a','b','c'])}")


# ============================================
# PRACTICE EXERCISES
# ============================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# Exercise 1: Create a caching decorator
def cache_decorator(func):
    """Cache function results"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"  Cache hit for {args}")
            return cache[args]
        print(f"  Computing for {args}")
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper

@cache_decorator
def expensive_operation(x):
    time.sleep(0.5)  # Simulate expensive operation
    return x * x

print("\nCaching example:")
print(f"Result: {expensive_operation(5)}")
print(f"Result: {expensive_operation(5)}")  # Should be cached
print(f"Result: {expensive_operation(6)}")

# Exercise 2: Generator for prime numbers
def prime_generator():
    """Generate prime numbers infinitely"""
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

primes = prime_generator()
print(f"\nFirst 10 primes: {[next(primes) for _ in range(10)]}")

# Exercise 3: Recursive directory scanner (conceptual)
def recursive_sum(data):
    """Sum all numbers in nested structure"""
    total = 0
    if isinstance(data, (int, float)):
        return data
    elif isinstance(data, (list, tuple)):
        for item in data:
            total += recursive_sum(item)
    return total

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
print(f"\nRecursive sum: {recursive_sum(nested_numbers)}")

print("\n" + "=" * 50)
print("END OF LESSON 3 - FUNCTIONS AND MODULES")
print("=" * 50)
