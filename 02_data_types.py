# ==========================================
# Topic: Data Types
# By: Rania Rashid — BS AI, Ghazi University
# ==========================================

# Python has several built-in data types
# Each type stores a different kind of data

# 1. Declare one variable of each type: int, float, str, bool
integer_var = 42                   # integer (whole number)
float_var = 3.14                   # float (decimal number)
string_var = "Hello, Python!"      # string (text)
boolean_var = True                 # boolean (True or False)

# 2. Print each variable AND its type using type()
print(f"Integer: {integer_var}, Type: {type(integer_var)}")
print(f"Float: {float_var}, Type: {type(float_var)}")
print(f"String: {string_var}, Type: {type(string_var)}")
print(f"Boolean: {boolean_var}, Type: {type(boolean_var)}")

# 3. Type casting: convert a float to int, print both
# int() removes the decimal part — it truncates, not rounds (5.99 becomes 5, not 6)
original_float = 5.99
int_from_float = int(original_float)
print(f"Float: {original_float}, Type: {type(original_float)}")
print(f"Integer: {int_from_float}, Type: {type(int_from_float)}")

# 4. Fix this code and explain why it crashes in a comment
# Crashes because Python cannot concatenate str and int directly
# + operator requires both sides to be the same type
# Fix: cast age to str using str()
name = "Rania"
age = 20
print(name + str(age))

# 5. Take user input, convert to float, multiply by 2, print result
# input() always returns a string — must cast to float before math
user_input = input("Enter a number: ")
user_input_float = float(user_input)
result = user_input_float * 2
print(f"Result: {result}")

# ==========================================
# What I learned today:
# 1. Python has 4 basic data types: int, float, str, and bool
# 2. type() reveals the data type of any variable at runtime
# 3. Type casting converts between types but can lose data (float to int truncates)
# 4. Python cannot mix types in operations — str + int crashes without casting
# 5. user input() always returns a string and must be cast for mathematical use
# ==========================================