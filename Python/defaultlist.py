# Normal dictionary
from collections import defaultdict

student_grades = {}
grades = [
    ('elliot', 91),
    ('neelam', 98),
    ('bianca', 81),
    ('elliot', 88),
]

for name, grade in grades:
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)
print(student_grades)

student_grades = defaultdict(list)
for name, grade in grades:
    student_grades[name].append(grade)
print(student_grades)
