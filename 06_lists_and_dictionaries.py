# ============================================================
# Topic   : 06 — Lists & Dictionaries in Python
# Author  : Rania Rashid
# Ghazi University DG Khan — BS AI (2025–2029)
# ============================================================


# ─────────────────────────────────────────────
# CONCEPT 1: What is a List?
# A list is an ordered, mutable collection of items.
# Lists can contain different data types.
# ─────────────────────────────────────────────

# Create a list
fruits = ["apple", "banana", "orange", "grape"]
print("Fruits list:", fruits)

# Access list items by index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# List length
print("Number of fruits:", len(fruits))


# ─────────────────────────────────────────────
# CONCEPT 2: List Methods (Add, Remove, Modify)
# Lists have built-in methods to manipulate data.
# ─────────────────────────────────────────────

# Add items to a list
fruits.append("mango")
print("After append:", fruits)

# Insert at a specific position
fruits.insert(1, "blueberry")
print("After insert:", fruits)

# Remove an item
fruits.remove("blueberry")
print("After remove:", fruits)

# Modify an item
fruits[0] = "pineapple"
print("After modify:", fruits)


# ─────────────────────────────────────────────
# CONCEPT 3: List Slicing
# Extract a portion of a list using slice notation.
# ─────────────────────────────────────────────

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", numbers)

# Get items from index 2 to 5
print("Slice [2:5]:", numbers[2:5])

# Get every second item
print("Every second item:", numbers[::2])

# Get last 3 items
print("Last 3 items:", numbers[-3:])


# ─────────────────────────────────────────────
# CONCEPT 4: What is a Dictionary?
# A dictionary is an unordered, mutable collection of key-value pairs.
# Keys are unique, and values can be any data type.
# ─────────────────────────────────────────────

# Create a dictionary
student = {
    "name": "Rania Rashid",
    "age": 20,
    "university": "Ghazi University",
    "program": "BS AI"
}
print("Student dictionary:", student)

# Access values by key
print("Student name:", student["name"])
print("Student age:", student["age"])


# ─────────────────────────────────────────────
# CONCEPT 5: Dictionary Methods (Add, Remove, Modify)
# Manipulate dictionary key-value pairs.
# ─────────────────────────────────────────────

# Add a new key-value pair
student["city"] = "DG Khan"
print("After adding city:", student)

# Modify an existing value
student["age"] = 21
print("After modifying age:", student)

# Remove a key-value pair
del student["city"]
print("After deleting city:", student)

# Get all keys
print("All keys:", student.keys())

# Get all values
print("All values:", student.values())


# ─────────────────────────────────────────────
# CONCEPT 6: Looping Through Lists & Dictionaries
# Iterate over collections to process each item.
# ─────────────────────────────────────────────

# Loop through a list
print("\nFruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Loop through a dictionary
print("\nStudent Information:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Loop through dictionary keys only
print("\nDictionary keys:")
for key in student:
    print(f"  - {key}")
