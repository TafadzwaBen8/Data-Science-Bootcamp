# Project: Student Performance Analyzer
# By : Tafadzwa Ben
# Course : Python Fundamentals

print("=" * 50)
print("      STUDENT PERFORMANCE ANALYZER")
print("=" * 50)
print()

# ==================================================
# Student Information
# ==================================================
student_name = input("Enter your name:")
student_program = input("What is your program:")

print("=" * 50)

print("Welcome,: {}!".format(student_name))
print("Program: {} ".format(student_program))


print("-" * 50)

# ==================================================
# Subject Marks
# ==================================================

def get_mark(subject):
    while True:
        mark = float(input("Enter {} mark (0-100): ".format(subject)))
        if 0 <= mark <= 100:
            return mark
        print("Mark must be between 0 and 100.")

digital_electronic_mark = get_mark("Digital Electronics")
data_science_mark = get_mark("Data Science")
python_mark = get_mark("Python")
machine_learning_mark = get_mark("Machine Learning")

# ==================================================
# Calculations
# ==================================================

print("-" * 50)


total = (
    digital_electronic_mark
    + data_science_mark
    + python_mark
    + machine_learning_mark
)

average = float(total / 4)

print("Total: {}".format(total))
print("Average: {:.2f}".format(average))


# ==================================================
# Grade Calculation
# ==================================================


if average >=80:
    grade = "Distinction"
elif average >=65:
    grade = "Merit"
elif average >= 50:
    grade = "Pass"
else :
    grade = "Fail"

if average >= 50:
    status = "Pass"
else:
    status = "Fail"

print("Grade: {}".format(grade))
print("Status: {}".format(status))


print("=" * 50)
print("      STUDENT PERFORMANCE REPORT")
print("=" * 50)