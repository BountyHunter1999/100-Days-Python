import random

names = ["Ram", "Shyam", "Hari", "Bibek", "Dakota"]
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students_with_score = {student: score for (student, score) in student_scores.items() if score >= 50}
print(passed_students_with_score)
