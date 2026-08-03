"""
Data Structures - Intermediate Python Lesson 2
================================================

This lesson covers essential data structures for intermediate Python programming.

Topics Covered:
1. Advanced List Operations
2. Dictionaries Deep Dive
3. Sets and Set Operations
4. Collections Module (Counter, defaultdict, deque)
5. List Comprehensions
6. Nested Data Structures
"""

# ============================================
# 1. ADVANCED LIST OPERATIONS
# ============================================

print("=" * 50)
print("ADVANCED LIST OPERATIONS")
print("=" * 50)

# List methods
fruits = ["apple", "banana", "cherry"]

# append(), extend(), insert()
fruits.append("date")
print(f"After append: {fruits}")

fruits.extend(["elderberry", "fig"])
print(f"After extend: {fruits}")

fruits.insert(2, "blueberry")
print(f"After insert: {fruits}")

# remove(), pop(), clear()
fruits.remove("banana")
print(f"After remove: {fruits}")

last = fruits.pop()
print(f"Popped: {last}, Remaining: {fruits}")

# index(), count()
print(f"Index of 'cherry': {fruits.index('cherry')}")
print(f"Count of 'apple': {fruits.count('apple')}")

# sort(), sorted(), reverse()
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(f"Sorted: {numbers}")

numbers.sort(reverse=True)
print(f"Reverse sorted: {numbers}")

# Sorting with key
words = ["python", "is", "awesome", "a"]
words.sort(key=len)
print(f"Sorted by length: {words}")

# Slicing advanced
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Every 3rd: {data[::3]}")
print(f"Last 3: {data[-3:]}")
print(f"Reverse: {data[::-1]}")


# ============================================
# 2. DICTIONARIES DEEP DIVE
# ============================================

print("\n" + "=" * 50)
print("DICTIONARIES DEEP DIVE")
print("=" * 50)

# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"],
    "grades": {"Math": 95, "Physics": 88}
}

# Accessing values
print(f"Name: {student['name']}")
print(f"Using get(): {student.get('age', 'Not found')}")
print(f"Default value: {student.get('phone', 'Not provided')}")

# Adding/Updating
student["email"] = "alice@example.com"
student.update({"age": 21, "city": "New York"})
print(f"Updated: {student}")

# Dictionary methods
keys = student.keys()
values = student.values()
items = student.items()

print(f"Keys: {list(keys)}")
print(f"Values: {list(values)}")

# Looping through dictionaries
print("\nStudent Info:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(f"\nSquares: {squares}")

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"Merged: {merged}")


# ============================================
# 3. SETS AND SET OPERATIONS
# ============================================

print("\n" + "=" * 50)
print("SETS AND SET OPERATIONS")
print("=" * 50)

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union, Intersection, Difference
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Symmetric Difference: {set1 ^ set2}")

# Set methods
set1.add(6)
print(f"After add(6): {set1}")

set1.update([7, 8])
print(f"After update: {set1}")

set1.discard(8)
print(f"After discard(8): {set1}")

# Set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Practical: Remove duplicates from list
numbers_with_dup = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = list(set(numbers_with_dup))
print(f"Unique numbers: {unique_numbers}")


# ============================================
# 4. COLLECTIONS MODULE
# ============================================

print("\n" + "=" * 50)
print("COLLECTIONS MODULE")
print("=" * 50)

from collections import Counter, defaultdict, deque, OrderedDict

# Counter - Count occurrences
text = "hello world"
char_count = Counter(text)
print(f"Character count: {char_count}")
print(f"Most common 3: {char_count.most_common(3)}")

# defaultdict - Default values
word_lengths = defaultdict(int)
words = ["apple", "banana", "cherry", "date"]
for word in words:
    word_lengths[len(word)] += 1
print(f"Word lengths count: {dict(word_lengths)}")

# Group by first letter
by_first_letter = defaultdict(list)
for word in words:
    by_first_letter[word[0]].append(word)
print(f"Grouped by first letter: {dict(by_first_letter)}")

# deque - Double-ended queue (efficient append/pop from both ends)
queue = deque([1, 2, 3])
queue.appendleft(0)
queue.append(4)
print(f"Deque: {queue}")
print(f"Popleft: {queue.popleft()}")
print(f"After popleft: {queue}")

# OrderedDict - Maintains insertion order (now default in Python 3.7+)
ordered = OrderedDict()
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3
print(f"OrderedDict: {ordered}")


# ============================================
# 5. LIST COMPREHENSIONS
# ============================================

print("\n" + "=" * 50)
print("LIST COMPREHENSIONS")
print("=" * 50)

# Basic comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# With condition
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")

# Nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened: {flattened}")

# Complex example
names = ["alice", "bob", "charlie"]
uppercase = [name.upper() for name in names if len(name) > 3]
print(f"Uppercase (len>3): {uppercase}")

# Dictionary comprehension
word_len = {word: len(word) for word in words}
print(f"Word lengths dict: {word_len}")

# Set comprehension
unique_lengths = {len(word) for word in words}
print(f"Unique lengths: {unique_lengths}")


# ============================================
# 6. NESTED DATA STRUCTURES
# ============================================

print("\n" + "=" * 50)
print("NESTED DATA STRUCTURES")
print("=" * 50)

# Complex nested structure
company = {
    "name": "Tech Corp",
    "departments": [
        {
            "name": "Engineering",
            "employees": [
                {"name": "Alice", "role": "Developer", "skills": ["Python", "JavaScript"]},
                {"name": "Bob", "role": "Designer", "skills": ["Figma", "CSS"]}
            ]
        },
        {
            "name": "Marketing",
            "employees": [
                {"name": "Charlie", "role": "Manager", "skills": ["SEO", "Content"]}
            ]
        }
    ]
}

# Accessing nested data
print(f"Company: {company['name']}")
print(f"First department: {company['departments'][0]['name']}")
print(f"Alice's skills: {company['departments'][0]['employees'][0]['skills']}")

# Iterating through nested structures
print("\nAll employees:")
for dept in company["departments"]:
    print(f"\n{dept['name']}:")
    for emp in dept["employees"]:
        print(f"  - {emp['name']} ({emp['role']})")

# Finding specific data
python_devs = []
for dept in company["departments"]:
    for emp in dept["employees"]:
        if "Python" in emp["skills"]:
            python_devs.append(emp["name"])

print(f"\nPython developers: {python_devs}")

# Practical: Student database
students_db = [
    {"id": 1, "name": "Alice", "grades": {"math": 95, "science": 88}},
    {"id": 2, "name": "Bob", "grades": {"math": 78, "science": 92}},
    {"id": 3, "name": "Charlie", "grades": {"math": 85, "science": 85}}
]

# Calculate average math grade
math_grades = [s["grades"]["math"] for s in students_db]
avg_math = sum(math_grades) / len(math_grades)
print(f"\nAverage Math Grade: {avg_math:.2f}")

# Find top performer in each subject
print("\nTop performers:")
for subject in ["math", "science"]:
    top_student = max(students_db, key=lambda s: s["grades"][subject])
    print(f"  {subject.capitalize()}: {top_student['name']} ({top_student['grades'][subject]})")


# ============================================
# PRACTICE EXERCISES
# ============================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# Exercise 1: Word Frequency Counter
def word_frequency(text):
    """Count frequency of each word"""
    words = text.lower().split()
    # Remove punctuation
    cleaned_words = [word.strip(".,!?;:") for word in words]
    return Counter(cleaned_words)

sample_text = "Python is great. Python is fun. Learning Python is awesome!"
freq = word_frequency(sample_text)
print(f"Word frequency: {dict(freq)}")

# Exercise 2: Flatten nested list
def flatten_nested_list(nested_list):
    """Flatten any level of nested lists"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    return result

nested = [1, [2, [3, 4], 5], [6, [7, 8]]]
print(f"Flattened: {flatten_nested_list(nested)}")

# Exercise 3: Group anagrams
def group_anagrams(words):
    """Group words that are anagrams of each other"""
    anagram_groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word.lower()))
        anagram_groups[key].append(word)
    return dict(anagram_groups)

word_list = ["listen", "silent", "triangle", "integral", "apple", "pale"]
print(f"Anagram groups: {group_anagrams(word_list)}")

print("\n" + "=" * 50)
print("END OF LESSON 2 - DATA STRUCTURES")
print("=" * 50)
