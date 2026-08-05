# ============================================================
# Topic   : 08 — File Handling in Python
# Author  : Rania Rashid
# Ghazi University DG Khan — BS AI (2025–2029)
# ============================================================

# ─────────────────────────────────────────────
# CONCEPT 1: Opening a file for writing
# 'w' mode creates a file or replaces existing content.
# ─────────────────────────────────────────────

file_name = "sample_text.txt"
print(f"Writing to file: {file_name}")

with open(file_name, "w", encoding="utf-8") as file:
    file.write("Hello, Python file handling!\n")
    file.write("This is the first line.\n")
    file.write("This file was created using Python.\n")

print("File created and written successfully.\n")

# ─────────────────────────────────────────────
# CONCEPT 2: Reading the full file content
# 'r' mode reads the file. Use read() to get all text.
# ─────────────────────────────────────────────

with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

print("Full file content:")
print(content)

# ─────────────────────────────────────────────
# CONCEPT 3: Reading line by line
# readlines() returns a list of lines.
# ─────────────────────────────────────────────

with open(file_name, "r", encoding="utf-8") as file:
    lines = file.readlines()

print("File lines:")
for line in lines:
    print(line.strip())

# ─────────────────────────────────────────────
# CONCEPT 4: Appending text to a file
# 'a' mode adds new content without removing existing text.
# ─────────────────────────────────────────────

with open(file_name, "a", encoding="utf-8") as file:
    file.write("\nThis line was appended later.\n")

print("Appended a new line to the file.\n")

# ─────────────────────────────────────────────
# CONCEPT 5: Counting words in a file
# Use split() to measure simple word count.
# ─────────────────────────────────────────────

with open(file_name, "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()
print(f"Word count: {len(words)}")

# ─────────────────────────────────────────────
# CONCEPT 6: Using try/except for file errors
# Handle cases where the file cannot be opened.
# ─────────────────────────────────────────────

try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename.")

# ─────────────────────────────────────────────
# What I learned today:
# 1. Use open() with modes: 'r', 'w', and 'a'.
# 2. with open(...) ensures the file closes automatically.
# 3. read() gets full text, readlines() returns lines.
# 4. append mode adds content without deleting existing text.
# 5. split() is useful for counting words in a file.
# ============================================================
