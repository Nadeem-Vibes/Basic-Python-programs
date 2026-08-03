"""
String Manipulation - Intermediate Python Lesson 1
===================================================

This lesson covers advanced string operations that are essential for 
real-world Python programming.

Topics Covered:
1. String Formatting (f-strings, format(), %)
2. String Methods (split, join, strip, replace, find)
3. String Slicing and Indexing
4. Regular Expressions Basics
5. Multi-line Strings
6. String Encoding/Decoding
"""

# ============================================
# 1. STRING FORMATTING
# ============================================

print("=" * 50)
print("STRING FORMATTING")
print("=" * 50)

# Method 1: f-strings (Python 3.6+) - RECOMMENDED
name = "Alice"
age = 25
height = 5.7

# Basic f-string
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# f-string with expressions
print(f"Next year, I will be {age + 1}")

# f-string with formatting (decimal places)
print(f"Height: {height:.2f} feet")

# f-string with padding
print(f"Name: {name:>10} | Age: {age:<5}")

# Method 2: format() method
template = "Hello, {}! You are {} years old."
print(template.format(name, age))

# With named placeholders
template_named = "Hello, {name}! You are {age} years old."
print(template_named.format(name="Bob", age=30))

# Method 3: % formatting (older style, still used)
print("Hello, %s! You are %d years old." % (name, age))


# ============================================
# 2. STRING METHODS
# ============================================

print("\n" + "=" * 50)
print("STRING METHODS")
print("=" * 50)

text = "  Hello, World! Welcome to Python Programming.  "

# strip(), lstrip(), rstrip() - Remove whitespace
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")

# upper(), lower(), title(), capitalize()
print(f"Upper: {text.strip().upper()}")
print(f"Lower: {text.strip().lower()}")
print(f"Title: {text.strip().title()}")

# split() - Split string into list
words = text.strip().split()
print(f"Split by space: {words}")

sentence = "apple,banana,cherry,date"
fruits = sentence.split(",")
print(f"Split by comma: {fruits}")

# join() - Join list into string
joined = " - ".join(words)
print(f"Joined with ' - ': {joined}")

# replace() - Replace substrings
replaced = text.replace("World", "Universe")
print(f"Replaced: {replaced.strip()}")

# find(), index(), count()
print(f"Find 'Python': {text.find('Python')}")
print(f"Count 'o': {text.count('o')}")

# startswith(), endswith()
print(f"Starts with 'Hello': {text.strip().startswith('Hello')}")
print(f"Ends with 'Programming': {text.strip().endswith('Programming')}")

# isalpha(), isdigit(), isalnum()
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")


# ============================================
# 3. STRING SLICING AND INDEXING
# ============================================

print("\n" + "=" * 50)
print("STRING SLICING AND INDEXING")
print("=" * 50)

text = "PythonProgramming"

# Basic indexing
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")

# Slicing [start:end:step]
print(f"First 6 chars: {text[0:6]}")
print(f"From index 6: {text[6:]}")
print(f"Every 2nd char: {text[::2]}")
print(f"Reverse: {text[::-1]}")

# Practical example - Extract domain from email
email = "user@example.com"
domain = email.split("@")[1].split(".")[0]
print(f"Email domain: {domain}")


# ============================================
# 4. REGULAR EXPRESSIONS BASICS
# ============================================

print("\n" + "=" * 50)
print("REGULAR EXPRESSIONS BASICS")
print("=" * 50)

import re

text = "Contact us at support@example.com or sales@company.org. Phone: 123-456-7890"

# Find all emails
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(f"Emails found: {emails}")

# Find phone numbers (simple pattern)
phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(f"Phone numbers: {phones}")

# Replace patterns
masked = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
print(f"Masked: {masked}")

# Validate email
def is_valid_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    return bool(re.match(pattern, email))

print(f"Is 'test@email.com' valid? {is_valid_email('test@email.com')}")
print(f"Is 'invalid-email' valid? {is_valid_email('invalid-email')}")


# ============================================
# 5. MULTI-LINE STRINGS
# ============================================

print("\n" + "=" * 50)
print("MULTI-LINE STRINGS")
print("=" * 50)

# Using triple quotes
paragraph = """This is a multi-line string.
It can span multiple lines.
Very useful for documentation!"""

print(paragraph)

# Escape characters
print("\nEscape characters:")
print("Newline: \\n")
print("Tab: \\t")
print("Quote: \\'")
print("Backslash: \\\\")


# ============================================
# 6. STRING ENCODING/DECODING
# ============================================

print("\n" + "=" * 50)
print("STRING ENCODING/DECODING")
print("=" * 50)

# Encode string to bytes
text = "Hello, 世界"
encoded = text.encode('utf-8')
print(f"Encoded: {encoded}")

# Decode bytes back to string
decoded = encoded.decode('utf-8')
print(f"Decoded: {decoded}")

# Base64 encoding (for data transmission)
import base64
original = "Secret Message"
base64_encoded = base64.b64encode(original.encode()).decode()
print(f"Base64: {base64_encoded}")
base64_decoded = base64.b64decode(base64_encoded).decode()
print(f"Base64 Decoded: {base64_decoded}")


# ============================================
# PRACTICE EXERCISES
# ============================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# Exercise 1: Password Validator
def validate_password(password):
    """Check if password meets requirements"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not re.search(r'[A-Z]', password):
        return False, "Must contain uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Must contain lowercase letter"
    if not re.search(r'\d', password):
        return False, "Must contain a number"
    return True, "Valid password"

test_passwords = ["weak", "Strong1", "PASSWORD123", "GoodPass123"]
for pwd in test_passwords:
    is_valid, message = validate_password(pwd)
    print(f"'{pwd}': {message}")

# Exercise 2: Text Analyzer
def analyze_text(text):
    """Analyze text statistics"""
    words = text.split()
    return {
        'characters': len(text),
        'words': len(words),
        'sentences': text.count('.') + text.count('!') + text.count('?'),
        'avg_word_length': sum(len(word) for word in words) / len(words) if words else 0
    }

sample_text = "Python is amazing. It makes programming fun! Try it today."
stats = analyze_text(sample_text)
print(f"\nText Analysis: {stats}")

print("\n" + "=" * 50)
print("END OF LESSON 1 - STRING MANIPULATION")
print("=" * 50)
