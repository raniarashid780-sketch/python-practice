# ============================================================
# Topic   : 04 — Loops (for & while)
# Author  : Rania Rashid
# Ghazi University DG Khan — BS AI (2025–2029)
# ============================================================


# ─────────────────────────────────────────────
# CONCEPT 1: for loop with range()
# Repeats a block of code a specific number of times.
# range(start, stop, step) — stop is EXCLUSIVE
# ─────────────────────────────────────────────

# Simple counting loop (0 to 4)
print("Counting from 0 to 4:")
for i in range(5):
    print(i)

print()

# Counting with start and stop (2 to 7)
print("Counting from 2 to 7:")
for i in range(2, 8):
    print(i)

print()

# Counting with step (0 to 10, by 2s)
print("Even numbers 0 to 10:")
for i in range(0, 11, 2):
    print(i)


# ─────────────────────────────────────────────
# CONCEPT 2: for loop with list/string
# Iterate through each element in a collection.
# ─────────────────────────────────────────────

subjects = ["Python", "Math", "Physics", "AI"]
print("\nMy subjects:")
for subject in subjects:
    print(f"  - {subject}")

print()

# Loop through a string (each character)
name = "Rania"
print(f"Letters in '{name}':")
for letter in name:
    print(letter)


# ─────────────────────────────────────────────
# CONCEPT 3: while loop
# Repeats while a condition is True.
# Be careful of infinite loops!
# ─────────────────────────────────────────────

counter = 0
print("\nCounting with while loop:")
while counter < 5:
    print(counter)
    counter += 1  # Increment counter (counter = counter + 1)

print()

# Real-world example: password validation
# Keeps asking until correct password is entered
password = ""
correct_password = "python2025"
attempts = 0
while password != correct_password and attempts < 3:
    password = input("Enter password: ")
    attempts += 1
    if password == correct_password:
        print("✓ Access granted!")
    elif attempts < 3:
        print("✗ Wrong password. Try again.")
    else:
        print("✗ Too many attempts. Access denied.")


# ─────────────────────────────────────────────
# CONCEPT 4: break & continue
# break   → exits the loop immediately
# continue → skips the current iteration, goes to next
# ─────────────────────────────────────────────

print("\nLoop with break (stop at 5):")
for i in range(10):
    if i == 5:
        break  # Exit loop when i equals 5
    print(i)

print()

print("Loop with continue (skip 3 and 6):")
for i in range(10):
    if i == 3 or i == 6:
        continue  # Skip printing 3 and 6
    print(i)


# ─────────────────────────────────────────────
# CONCEPT 5: Nested loops
# A loop inside another loop.
# Example: multiplication table
# ─────────────────────────────────────────────

print("\n3×3 Multiplication Table:")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i}×{j}={result}", end="  ")  # end="  " prevents newline
    print()  # Newline after each row

print()

# Nested loop example: pattern printing
print("Star pattern:")
for i in range(1, 6):
    print("★" * i)  # Print i stars


# ─────────────────────────────────────────────
# CONCEPT 6: Loop with enumerate()
# Get both index AND value when iterating a list
# ─────────────────────────────────────────────

fruits = ["Apple", "Banana", "Cherry", "Date"]
print("\nFruits with indices:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


# ─────────────────────────────────────────────
# CONCEPT 7: Loop with zip()
# Iterate through two lists together
# ─────────────────────────────────────────────

names = ["Ali", "Fatima", "Hassan"]
ages = [20, 19, 21]
print("\nNames and ages:")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


# ============================================================
# What I learned today:
# 1. for loops repeat a block for a specific number of times
# 2. for loops can iterate through lists, strings, and ranges
# 3. while loops repeat while a condition is True (watch for infinite loops!)
# 4. break exits a loop; continue skips to the next iteration
# 5. Nested loops: loop inside loop (use for patterns, tables, etc.)
# 6. enumerate() gives both index and value when iterating
# 7. zip() iterates through multiple lists together
# ============================================================
