# ============================================================
# Topic   : 03 — Conditions & If/Else
# Author  : Rania Rashid
# Ghazi University DG Khan — BS AI (2025–2029)
# ============================================================


# ─────────────────────────────────────────────
# CONCEPT 1: Boolean Expressions
# A condition always evaluates to True or False.
# Operators: ==  !=  >  <  >=  <=
# ─────────────────────────────────────────────

print(5 > 3)   # True, because 5 is greater than 3
print(10 == 10) # True, because both sides are equal
print(7 <= 5)   # False, because 7 is not less than or equal to 5



# ─────────────────────────────────────────────
# CONCEPT 2: if / elif / else
# Python uses indentation (4 spaces) to define blocks.
# There is NO {} like other languages — indentation IS the syntax.
# ─────────────────────────────────────────────

score = 85  # You can change this value to test different cases
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")

# ─────────────────────────────────────────────
# CONCEPT 3: Nested Conditions (Method 1)
# A condition inside another condition.
# WARNING: Deep nesting makes code unreadable — know when to stop.
# ─────────────────────────────────────────────

voter_age = int(input("Enter your age: "))
is_registered = input("Are you registered to vote? (yes/no): ").lower() == "yes"
if voter_age >= 18:
    if is_registered:
        print("You are eligible to vote!")
    else:
        print("You are eligible but not registered to vote.")
else:
    print("You are not eligible to vote yet.")


# ─────────────────────────────────────────────
# CONCEPT 4: Logical Operators (Better Method)
# and  → both conditions must be True
# or   → at least one must be True
# not  → flips True to False, False to True
# This is CLEANER than nested conditions above!
# ─────────────────────────────────────────────

# Using logical operators (same problem, cleaner code):
voter_age = int(input("Enter your age: "))
is_registered = input("Are you registered to vote? (yes/no): ").lower() == "yes"
if voter_age >= 18 and is_registered:
    print("You are eligible to vote!")
elif voter_age >= 18 and not is_registered:
    print("You are eligible but not registered to vote.")
else:
    print("You are not eligible to vote yet.")      



# ─────────────────────────────────────────────
# CONCEPT 5: Ternary (One-Line If)
# Syntax: value_if_true if condition else value_if_false
# Use ONLY when it improves readability — not to show off.
# ─────────────────────────────────────────────

score = 60
result = "Pass" if score >= 50 else "Fail"
print(result)

# ─────────────────────────────────────────────
# CONCEPT 6: Real Mini-Problem
# Write a grade classifier function — but do NOT define functions yet.
# Use only variables + conditions for now.
# ─────────────────────────────────────────────

subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))
average = (subject1 + subject2 + subject3) / 3
if average >= 85:
    classification = "Distinction"
elif average >= 70:
    classification = "Merit"
elif average >= 50:
    classification = "Pass"
else:
    classification = "Fail"
print(f"Average: {average:.2f}, Classification: {classification}")


# ============================================================
# WHAT I LEARNED TODAY
# ============================================================
# 1. Conditions evaluate to True or False using comparison operators.
# 2. if/elif/else blocks control the flow of code based on conditions.
# 3. Nested conditions can check multiple layers of logic but can reduce readability.
# 4. Logical operators (and, or, not) combine multiple conditions into one.
# 5. Ternary operators allow for concise conditional assignments but should be used judiciously.
# ============================================================
