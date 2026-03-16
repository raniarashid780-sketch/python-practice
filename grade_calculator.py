# ==========================================
# Project: Student Grade Calculator
# By: Rania Rashid — BS AI, Ghazi University
# Semester 2 — 100 Days of Code
# ==========================================
# Function ONLY calculates — nothing else

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average
def get_grade(average):
    
    if 90 <= average <= 100:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average  < 80:
        return "C"
    elif 60 <= average < 70 :
        return "D"
    else:
        return "F"
# Input collection happens OUTSIDE
marks = []
for i in range(5):
    marks.append(float(input(f"Enter mark {i+1}: ")))

# Pass the collected list INTO the function
average = calculate_average(marks)
print(f"The average marks is: {average}")
grade = get_grade(average)
print(f"The grade is: {grade}")