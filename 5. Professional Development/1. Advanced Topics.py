"""
Professional Development - Advanced Python Topics
==================================================

This section covers professional-level Python concepts used in 
production environments and enterprise applications.

Topics Covered:
1. Async/Await (Asynchronous Programming)
2. Context Managers
3. Metaclasses
4. Type Hinting and Static Analysis
5. Testing with pytest
6. Logging Best Practices
7. Performance Optimization
8. Design Patterns
"""

# ============================================
# 1. ASYNCHRONOUS PROGRAMMING
# ============================================

print("=" * 50)
print("ASYNCHRONOUS PROGRAMMING")
print("=" * 50)

import asyncio
import time

# Synchronous vs Asynchronous

def sync_function():
    """Synchronous - blocks execution"""
    print("Sync: Starting...")
    time.sleep(1)  # Blocks everything
    print("Sync: Done!")

async def async_function():
    """Asynchronous - allows other tasks to run"""
    print("Async: Starting...")
    await asyncio.sleep(1)  # Non-blocking
    print("Async: Done!")

# Running async code
async def main_async():
    # Run multiple async functions concurrently
    await asyncio.gather(
        async_function(),
        async_function(),
        async_function()
    )

# Uncomment to run:
# asyncio.run(main_async())

# Practical: Async web scraper simulation
async def fetch_url(url, delay=1):
    """Simulate fetching a URL"""
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def scrape_multiple_urls():
    urls = [
        "https://api.example.com/users",
        "https://api.example.com/posts",
        "https://api.example.com/comments"
    ]
    
    # Sequential (slow)
    start = time.time()
    results_seq = [await fetch_url(url) for url in urls]
    print(f"Sequential: {time.time() - start:.2f}s")
    
    # Concurrent (fast)
    start = time.time()
    results_conc = await asyncio.gather(*[fetch_url(url) for url in urls])
    print(f"Concurrent: {time.time() - start:.2f}s")
    
    return results_conc

# asyncio.run(scrape_multiple_urls())


# ============================================
# 2. CONTEXT MANAGERS
# ============================================

print("\n" + "=" * 50)
print("CONTEXT MANAGERS")
print("=" * 50)

# Using 'with' statement
class DatabaseConnection:
    """Custom context manager for database connections"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to {self.db_name}...")
        self.connection = f"Connection({self.db_name})"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}...")
        self.connection = None
        if exc_type:
            print(f"Error occurred: {exc_val}")
        return False  # Don't suppress exceptions

# Usage
with DatabaseConnection("mydb") as conn:
    print(f"Using {conn}")
    # Connection automatically closed after block

# Context manager with contextlib
from contextlib import contextmanager

@contextmanager
def timer(name="Operation"):
    """Time how long a block takes"""
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{name} took {end - start:.4f} seconds")

with timer("Calculation"):
    sum(range(1000000))

# Multiple context managers
with DatabaseConnection("db1") as conn1, \
     DatabaseConnection("db2") as conn2:
    print(f"Connected to {conn1} and {conn2}")


# ============================================
# 3. METACLASSES
# ============================================

print("\n" + "=" * 50)
print("METACLASSES")
print("=" * 50)

# A metaclass is a class of a class
class SingletonMeta(type):
    """Metaclass that creates singleton classes"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "DB Connection"

# Both instances are the same object
db1 = Database()
db2 = Database()
print(f"Same instance: {db1 is db2}")

# Validation metaclass
class ValidateMeta(type):
    """Metaclass that validates class attributes"""
    def __new__(mcs, name, bases, attrs):
        # Ensure all classes have a 'description' attribute
        if 'description' not in attrs:
            raise TypeError(f"{name} must have a 'description' attribute")
        
        # Convert string descriptions to uppercase
        if isinstance(attrs.get('description'), str):
            attrs['description'] = attrs['description'].upper()
        
        return super().__new__(mcs, name, bases, attrs)

class Product(metaclass=ValidateMeta):
    description = "A sample product"
    
    def get_description(self):
        return self.description

print(f"Product description: {Product().get_description()}")


# ============================================
# 4. TYPE HINTING AND STATIC ANALYSIS
# ============================================

print("\n" + "=" * 50)
print("TYPE HINTING AND STATIC ANALYSIS")
print("=" * 50)

from typing import List, Dict, Optional, Union, Callable, Tuple, Any, Generic, TypeVar

# Basic type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Complex types
def process_data(
    items: List[int],
    mapping: Dict[str, float],
    optional_value: Optional[str] = None
) -> Union[int, str]:
    if optional_value:
        return optional_value
    return sum(items)

# Function types
def apply_operation(
    values: List[float],
    operation: Callable[[float], float]
) -> List[float]:
    return [operation(v) for v in values]

print(apply_operation([1.0, 2.0, 3.0], lambda x: x * 2))

# Type aliases
Vector = List[float]
Matrix = List[Vector]

def transpose(matrix: Matrix) -> Matrix:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Generic types
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()

stack = Stack[int]()
stack.push(1)
stack.push(2)
print(f"Popped: {stack.pop()}")

# Protocol (structural subtyping)
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(shape: Drawable) -> None:
    shape.draw()

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

render(Circle())  # Works even though Circle doesn't explicitly implement Drawable


# ============================================
# 5. TESTING WITH PYTEST
# ============================================

print("\n" + "=" * 50)
print("TESTING WITH PYTEST")
print("=" * 50)

# Example test file structure (save as test_calculator.py):
"""
# test_calculator.py
import pytest

def add(a, b):
    return a + b

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_add_multiple_cases(a, b, expected):
    assert add(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
"""

# Fixtures example
"""
# conftest.py or in test file
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Test", "value": 42}

@pytest.fixture
def database_connection():
    # Setup
    db = connect_to_database()
    yield db
    # Teardown
    db.close()

def test_with_fixture(sample_data):
    assert sample_data["value"] == 42
"""

print("Pytest commands:")
print("  pytest                    # Run all tests")
print("  pytest -v                 # Verbose output")
print("  pytest test_file.py       # Run specific file")
print("  pytest -k 'test_name'     # Run matching tests")
print("  pytest --cov=.            # Coverage report")


# ============================================
# 6. LOGGING BEST PRACTICES
# ============================================

print("\n" + "=" * 50)
print("LOGGING BEST PRACTICES")
print("=" * 50)

import logging
from logging.handlers import RotatingFileHandler

# Configure logging
def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        'app.log', 
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

logger = setup_logging()

# Logging levels
logger.debug("Debug message - detailed info")
logger.info("Info message - general info")
logger.warning("Warning message - something unexpected")
logger.error("Error message - something went wrong")
logger.critical("Critical message - serious error")

# Logging with context
def process_item(item_id: int):
    logger.info(f"Processing item {item_id}")
    try:
        # Simulate processing
        result = item_id * 2
        logger.debug(f"Item {item_id} processed successfully")
        return result
    except Exception as e:
        logger.exception(f"Failed to process item {item_id}")
        raise

process_item(42)


# ============================================
# 7. PERFORMANCE OPTIMIZATION
# ============================================

print("\n" + "=" * 50)
print("PERFORMANCE OPTIMIZATION")
print("=" * 50)

# Use built-in functions (they're optimized in C)
numbers = list(range(1000000))

# Slow: Manual loop
start = time.time()
total = 0
for n in numbers:
    total += n
print(f"Manual loop: {time.time() - start:.4f}s")

# Fast: Built-in sum
start = time.time()
total = sum(numbers)
print(f"Built-in sum: {time.time() - start:.4f}s")

# List comprehension vs map
start = time.time()
squares = [x**2 for x in numbers]
print(f"List comprehension: {time.time() - start:.4f}s")

# Generators for memory efficiency
def get_squares_list(n):
    return [x**2 for x in range(n)]  # Creates full list in memory

def get_squares_generator(n):
    return (x**2 for x in range(n))  # Generates on demand

# Caching with lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
result = fibonacci(100)
print(f"Fibonacci(100) with cache: {time.time() - start:.4f}s")

# Using slots for memory optimization
class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ['x', 'y']  # Prevents dynamic attribute creation
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# String concatenation
# Slow: Repeated concatenation
result = ""
for i in range(10000):
    result += str(i)  # Creates new string each time

# Fast: Join
result = "".join(str(i) for i in range(10000))


# ============================================
# 8. DESIGN PATTERNS
# ============================================

print("\n" + "=" * 50)
print("DESIGN PATTERNS")
print("=" * 50)

# Observer Pattern
class Observer:
    def update(self, data) -> None:
        pass

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def notify(self, data) -> None:
        for observer in self._observers:
            observer.update(data)

class EmailNotifier(Observer):
    def update(self, data) -> None:
        print(f"Sending email: {data}")

class SMSNotifier(Observer):
    def update(self, data) -> None:
        print(f"Sending SMS: {data}")

# Usage
subject = Subject()
subject.attach(EmailNotifier())
subject.attach(SMSNotifier())
subject.notify("New order received!")

# Factory Pattern
class PaymentProcessor:
    def process(self, amount: float) -> None:
        pass

class StripeProcessor(PaymentProcessor):
    def process(self, amount: float) -> None:
        print(f"Processing ${amount} via Stripe")

class PayPalProcessor(PaymentProcessor):
    def process(self, amount: float) -> None:
        print(f"Processing ${amount} via PayPal")

class PaymentFactory:
    @staticmethod
    def create_processor(method: str) -> PaymentProcessor:
        if method == "stripe":
            return StripeProcessor()
        elif method == "paypal":
            return PayPalProcessor()
        raise ValueError(f"Unknown payment method: {method}")

processor = PaymentFactory.create_processor("stripe")
processor.process(99.99)

# Decorator Pattern (different from function decorators)
class Coffee:
    def cost(self) -> float:
        return 5.0
    
    def description(self) -> str:
        return "Coffee"

class CoffeeDecorator:
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    
    def cost(self) -> float:
        return self._coffee.cost()
    
    def description(self) -> str:
        return self._coffee.description()

class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 2.0
    
    def description(self) -> str:
        return self._coffee.description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.0
    
    def description(self) -> str:
        return self._coffee.description() + ", Sugar"

base_coffee = Coffee()
with_milk = MilkDecorator(base_coffee)
with_milk_and_sugar = SugarDecorator(with_milk)
print(f"{with_milk_and_sugar.description()} = ${with_milk_and_sugar.cost()}")


# ============================================
# SUMMARY AND NEXT STEPS
# ============================================

print("\n" + "=" * 50)
print("PROFESSIONAL DEVELOPMENT SUMMARY")
print("=" * 50)

print("""
Key Takeaways:

1. ASYNC PROGRAMMING
   - Use asyncio for I/O-bound operations
   - Great for web scraping, API calls, file operations
   
2. CONTEXT MANAGERS
   - Use 'with' for resource management
   - Create custom managers for cleanup logic

3. METACLASSES
   - Powerful but use sparingly
   - Good for framework development

4. TYPE HINTS
   - Improves code quality and IDE support
   - Use mypy for static analysis

5. TESTING
   - Write tests before/during development
   - Use fixtures for setup/teardown
   - Aim for high coverage

6. LOGGING
   - Never use print() in production
   - Use appropriate log levels
   - Include context in logs

7. PERFORMANCE
   - Profile before optimizing
   - Use built-ins and generators
   - Cache expensive operations

8. DESIGN PATTERNS
   - Know common patterns
   - Don't over-engineer
   - Solve actual problems

NEXT STEPS:
-----------
- Build real projects
- Contribute to open source
- Learn frameworks (Django, FastAPI)
- Study system design
- Practice algorithms
- Read Python documentation
""")

print("=" * 50)
print("END OF PROFESSIONAL DEVELOPMENT LESSON")
print("=" * 50)
