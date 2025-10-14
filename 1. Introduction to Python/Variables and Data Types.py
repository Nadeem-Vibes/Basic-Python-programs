'''
1) Before diving very deep, let's understand what is a variable :-
  · Variables are like containers that store data values.
  · In Python, you don’t need to specify the type of the variable; it automatically understands based on the value assigned.
  · Here are the examples...
'''

x = 10  # Integer variable
y = 3.14  # Float variable
name = "Your name"  # String variable
is_student = True  # Boolean variable

'''
If you type ' print(type(x)) ' it will show what variable it is using.
Note: Boolean consist only 'True' or 'False'
'''

'''
2) In Python there are many kinds of Data Types, let's learn one by one :-
  a) Numbers:-
    · Integers (Whole numbers like 1, 2, 100)
    · Floats (Decimal numbers like 3.14, 0.001)
    · Here are some examples...
'''

age = 16  # Integer
pi = 3.1415  # Float

''' Now here's a quick way to remember, if there is a decimal point, it is a Float or else it is a Integer. '''

'''
  b) Strings:-
    · They are the sequence of characters, used for text.
    · You can use single, double, or triple quotes.
    · Some examples...
'''

name = "Nadeem"  # Using double quotes
greeting = 'Hello!'  # Using single quotes
paragraph = '''This is
a multiline
string.'''  # Using triple quotes

'''
  c) Booleans:-
    · Very simple, Boolean consist only 'True' or 'False'.
    · Simple examples...
'''

is_python_fun = True
is_raining = False

''' Fun Fact: This is very easy to learn.'''

'''
  d) Lists:-
    · It is like a set of variables combined into one.
    · OR; a list is an ordered collection that can store different data types.
    · Example...
'''

my_list = [1, 2, "Python", 3.14, True]
print(my_list[2])  # Output: "Python"


''' It is used to store multiple values or strings into one group. '''

'''
  e) Tuples:-
    · All tuples are lists, only difference is that they are invincible (cannot be changed after creation).
    · Simple example...
'''

my_tuple = (10, "Hello", False)
print(my_tuple[1])  # Output: "Hello"

''' They are really powerful that no one can modify it. '''

'''
  f) Dictionary:-
    · They only store data in a Key-value pairs.
    · Exammpleee...
'''
my_dict = {"name": "Your name", "age": 16}
print(my_dict["name"])  # Output: "Your name"

''' Useful for storing data in one variable '''

'''
3) Variable Rules and Best Practices :-
  · Variable names should start with a letter or an underscore, not a number.
  · Use descriptive names (e.g., age, price, name_of_student) to make your code easier to read.
  · Make it simple like...
'''
# Good variable names:
student_name = "Nadeem"
total_price = 100.50

'''
4) Now the last one 'Type Casting' :-
  · You can convert one data type into another using type casting.
  · Likeeee...
'''
# Convert integer to string
age = 16
age_str = str(age)
print("Age: " + age_str)

# Convert string to float
num_str = "3.14"
num_float = float(num_str)

  
''' Okay that's all for the today's lesson see you. '''

'''
Here's a challenge for you
  · Create a variable for your name, age, and whether you’re a student.
  · Print out a sentence using those variables!
'''






''' If you appreciate my work, please consider supporting... '''
