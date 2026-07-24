# Project: NumPy Data Analysis Toolkit
# Author: Tafadzwa Ben
# Course: Python for Data Science and Machine Learning Bootcamp

import numpy as np


students = np.array([
    ["Tafadzwa", 85, 90, 78],
    ["Brian", 70, 65, 80],
    ["Mary", 95, 88, 92],
    ["John", 60, 75, 68],
    ["Anna", 88, 92, 85]
])


marks = students[:,1:].astype(float)

average_marks = np.mean(marks, axis=1)

class_average = np.mean(average_marks)

highest_index = np.argmax(average_marks)

highest_student = students[highest_index,0]


print("=" * 50)
print("        STUDENT PERFORMANCE SUMMARY")
print("=" * 50)

print("Class Average: {:.2f}".format(class_average))
print("Highest Performer: {}".format(highest_student))
print("Highest Score: {:.2f}".format(np.max(average_marks)))

print("-" * 50)

for student, marks in zip(students[:,0], average_marks):

    if marks >=75:
        grade = "Excellent"
    elif marks >=60:
        grade = "Good"
    elif marks >=50:
        grade = "Needs Improvement"
    else:
        grade = "Work Hard"

    print("{} - {} ({:.2f})".format(student, grade, marks))

print("=" * 50)