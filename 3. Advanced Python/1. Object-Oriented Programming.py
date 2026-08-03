"""
Object-Oriented Programming - Advanced Python Lesson 1
========================================================

This lesson covers OOP concepts from basics to advanced topics.

Topics Covered:
1. Classes and Objects Review
2. Inheritance and Polymorphism
3. Encapsulation and Abstraction
4. Magic Methods (Dunder Methods)
5. Property Decorators
6. Class Methods and Static Methods
7. Abstract Base Classes
8. Composition vs Inheritance
"""

# ============================================
# 1. CLASSES AND OBJECTS REVIEW
# ============================================

print("=" * 50)
print("CLASSES AND OBJECTS REVIEW")
print("=" * 50)

class Dog:
    """A simple Dog class"""
    
    # Class variable (shared by all instances)
    species = "Canine"
    
    def __init__(self, name, age):
        """Constructor - Instance variables"""
        self.name = name
        self.age = age
    
    def bark(self):
        """Instance method"""
        return f"{self.name} says Woof!"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())
print(dog2.get_info())
print(f"All dogs are {Dog.species}")


# ============================================
# 2. INHERITANCE AND POLYMORPHISM
# ============================================

print("\n" + "=" * 50)
print("INHERITANCE AND POLYMORPHISM")
print("=" * 50)

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this")
    
    def info(self):
        return f"I am {self.name}"

# Child classes
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
    def purr(self):
        return f"{self.name} is purring..."

class Bird(Animal):
    def speak(self):
        return f"{self.name} says Chirp!"
    
    def fly(self):
        return f"{self.name} is flying!"

# Polymorphism in action
animals = [Cat("Whiskers"), Bird("Tweety"), Cat("Garfield")]

for animal in animals:
    print(animal.speak())  # Same method, different behavior

# Check inheritance
print(f"\nCat is subclass of Animal: {issubclass(Cat, Animal)}")
print(f"Is instance: {isinstance(Cat('Fluffy'), Animal)}")


# ============================================
# 3. ENCAPSULATION AND ABSTRACTION
# ============================================

print("\n" + "=" * 50)
print("ENCAPSULATION AND ABSTRACTION")
print("=" * 50)

class BankAccount:
    """Demonstrates encapsulation with private variables"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private variable (name mangling)
        self.__account_number = self.__generate_account_number()
    
    def __generate_account_number(self):
        """Private method"""
        import random
        return str(random.randint(10000000, 99999999))
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Getter method to access private variable"""
        return f"Balance: ${self.__balance}"
    
    def get_account_info(self):
        return f"Account: {self.__account_number}, Owner: {self.owner}"

account = BankAccount("Alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
print(account.get_account_info())

# Try to access private variable (will fail)
# print(account.__balance)  # AttributeError!
print(f"Name mangled: {account._BankAccount__balance}")  # Not recommended


# ============================================
# 4. MAGIC METHODS (DUNDER METHODS)
# ============================================

print("\n" + "=" * 50)
print("MAGIC METHODS (DUNDER METHODS)")
print("=" * 50)

class Vector:
    """Demonstrates magic methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation for users"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Official representation for developers"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Addition operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        """Multiplication operator"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Equality operator"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """Length - magnitude of vector"""
        return int((self.x**2 + self.y**2)**0.5)
    
    def __getitem__(self, index):
        """Indexing support"""
        return [self.x, self.y][index]

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 * 3: {v1 * 3}")
print(f"v1 == v2: {v1 == v2}")
print(f"len(v1): {len(v1)}")
print(f"v1[0]: {v1[0]}")


# ============================================
# 5. PROPERTY DECORATORS
# ============================================

print("\n" + "=" * 50)
print("PROPERTY DECORATORS")
print("=" * 50)

class Temperature:
    """Demonstrates @property decorator"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Calculated property"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for calculated property"""
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")

temp.fahrenheit = 100
print(f"After setting F=100, Celsius: {temp.celsius:.2f}")


# ============================================
# 6. CLASS METHODS AND STATIC METHODS
# ============================================

print("\n" + "=" * 50)
print("CLASS METHODS AND STATIC METHODS")
print("=" * 50)

class Employee:
    """Demonstrates class and static methods"""
    
    num_employees = 0  # Class variable
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_employees += 1
        self.employee_id = Employee.num_employees
    
    def get_info(self):
        """Instance method"""
        return f"ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}"
    
    @classmethod
    def from_string(cls, employee_str):
        """Alternative constructor"""
        name, salary = employee_str.split(',')
        return cls(name.strip(), float(salary.strip()))
    
    @classmethod
    def get_total_employees(cls):
        """Class method accessing class variable"""
        return f"Total employees: {cls.num_employees}"
    
    @staticmethod
    def is_valid_salary(salary):
        """Static method - doesn't need self or cls"""
        return salary > 0
    
    @staticmethod
    def calculate_tax(salary, tax_rate=0.2):
        """Utility function"""
        return salary * tax_rate

emp1 = Employee("Alice", 50000)
emp2 = Employee.from_string("Bob, 60000")

print(emp1.get_info())
print(emp2.get_info())
print(Employee.get_total_employees())
print(f"Is valid salary: {Employee.is_valid_salary(50000)}")
print(f"Tax on $50000: ${Employee.calculate_tax(50000)}")


# ============================================
# 7. ABSTRACT BASE CLASSES
# ============================================

print("\n" + "=" * 50)
print("ABSTRACT BASE CLASSES")
print("=" * 50)

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class"""
    
    @abstractmethod
    def area(self):
        """Must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Must be implemented by subclasses"""
        pass
    
    def description(self):
        """Concrete method available to all subclasses"""
        return f"I am a {self.__class__.__name__}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

shapes = [Rectangle(5, 3), Circle(4)]

for shape in shapes:
    print(f"\n{shape.description()}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")

# Can't instantiate abstract class
# shape = Shape()  # TypeError!


# ============================================
# 8. COMPOSITION VS INHERITANCE
# ============================================

print("\n" + "=" * 50)
print("COMPOSITION VS INHERITANCE")
print("=" * 50)

# Composition example: A Car HAS an Engine
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine ({self.horsepower} HP) starting..."
    
    def stop(self):
        return "Engine stopped"

class Wheel:
    def __init__(self, size):
        self.size = size
    
    def rotate(self):
        return f"Wheel ({self.size}\") rotating"

class Car:
    """Composition: Car has Engine and Wheels"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = Engine(200)  # Has-a relationship
        self.wheels = [Wheel(18) for _ in range(4)]
    
    def drive(self):
        messages = []
        messages.append(self.engine.start())
        for wheel in self.wheels:
            messages.append(wheel.rotate())
        messages.append(f"{self.brand} {self.model} is driving!")
        return "\n".join(messages)
    
    def park(self):
        return f"{self.brand} {self.model} parked. {self.engine.stop()}"

my_car = Car("Tesla", "Model 3")
print(my_car.drive())
print(f"\n{my_car.park()}")

# Compare with inheritance
class Vehicle:
    """Base class for inheritance approach"""
    def move(self):
        return "Moving..."

class ElectricCar(Vehicle):
    """Inheritance approach"""
    def __init__(self):
        self.battery_level = 100
    
    def charge(self):
        return "Charging..."

print(f"\nElectric car: {ElectricCar().move()}")


# ============================================
# PRACTICE EXERCISES
# ============================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# Exercise 1: Library Management System
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} [{status}]"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        return f"Added: {book.title}"
    
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                return f"Borrowed: {book.title}"
        return "Book not available"
    
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                return f"Returned: {book.title}"
        return "Invalid return"
    
    def list_books(self):
        return [str(book) for book in self.books]

library = Library("City Library")
library.add_book(Book("Python Basics", "John Doe", "123"))
library.add_book(Book("Advanced Python", "Jane Smith", "456"))

print(library.borrow_book("123"))
print("\nLibrary Catalog:")
for book in library.list_books():
    print(f"  {book}")

# Exercise 2: Shopping Cart with Magic Methods
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def __len__(self):
        return sum(item['quantity'] for item in self.items.values())
    
    def __str__(self):
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return f"Cart ({len(self)} items) - Total: ${total:.2f}"

cart = ShoppingCart()
cart.add_item("Laptop", 999.99, 1)
cart.add_item("Mouse", 29.99, 2)
print(f"\n{cart}")

print("\n" + "=" * 50)
print("END OF LESSON 1 - OOP")
print("=" * 50)
