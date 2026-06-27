# ============================================================
# Topic   : 05 — Functions in Python
# Author  : Rania Rashid
# Ghazi University DG Khan — BS AI (2025–2029)
# ============================================================


# ─────────────────────────────────────────────
# CONCEPT 1: What is a Function?
# A function is a reusable block of code that performs a specific task.
# It helps keep programs organized, shorter, and easier to understand.
# ─────────────────────────────────────────────

# Define a simple function

def greet():
    print("Hello! Welcome to Python functions.")

# Call the function
print("Calling greet()...")
greet()


# ─────────────────────────────────────────────
# CONCEPT 2: Function with Parameters
# Parameters are inputs given to a function.
# They make functions more flexible and useful.
# ─────────────────────────────────────────────


def greet_name(name):
    print(f"Hello, {name}!")


greet_name("Rania")
greet_name("Ali")


# ─────────────────────────────────────────────
# CONCEPT 3: Function with Return Value
# A function can return a result to the place where it was called.
# return gives back data to the program.
# ─────────────────────────────────────────────


def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(f"5 + 7 = {result}")


# ─────────────────────────────────────────────
# CONCEPT 4: Function with Default Parameters
# Default values are used if no argument is passed.
# ─────────────────────────────────────────────


def introduce(name="Student", course="Python"):
    print(f"My name is {name} and I study {course}.")

introduce()
introduce("Fatima", "AI")


# ─────────────────────────────────────────────
# CONCEPT 5: Multiple Parameters
# A function can take more than one input.
# ─────────────────────────────────────────────


def calculate_area(length, width):
    area = length * width
    return area

area = calculate_area(6, 4)
print(f"Area = {area}")


# ─────────────────────────────────────────────
# CONCEPT 6: Real Mini-Problem
# Create a function that checks whether a number is even or odd.
# ─────────────────────────────────────────────


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))
print(check_even_odd(7))


# ─────────────────────────────────────────────
# CONCEPT 7: Function Calling Another Function
# Functions can be reused inside other functions.
# ─────────────────────────────────────────────


def welcome_user(name):
    return f"Welcome, {name}!"


def show_message(name):
    message = welcome_user(name)
    print(message)

show_message("Rania")


# ============================================================
# What I learned today:
# 1. Functions help organize code into reusable blocks.
# 2. Parameters allow functions to receive inputs.
# 3. return sends output back from a function.
# 4. Default parameters make functions more flexible.
# 5. Functions can be used to solve small problems cleanly.
# ============================================================
