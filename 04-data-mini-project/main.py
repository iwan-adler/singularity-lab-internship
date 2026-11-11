import csv
import numpy as np


def read_data(file_name):
    with open(file_name) as f:
        return list(csv.DictReader(f))


def clean_data(rows):
    students = []
    for row in rows:
        if "" in row.values():
            continue
        math = int(row["math score"])
        reading = int(row["reading score"])
        writing = int(row["writing score"])
        students.append({
            "gender": row["gender"],
            "lunch": row["lunch"],
            "prep": row["test preparation course"],
            "math": math,
            "reading": reading,
            "writing": writing,
            "average": (math + reading + writing) / 3,
        })
    return students


def average_by(students, column):
    groups = {}
    for s in students:
        groups.setdefault(s[column], []).append(s["average"])
    for name, scores in groups.items():
        print(name, round(np.mean(scores), 2))


def subject_stats(students):
    for subject in ["math", "reading", "writing"]:
        scores = np.array([s[subject] for s in students])
        print(subject, "- avg:", round(scores.mean(), 2), "max:", scores.max(), "min:", scores.min())


def pass_count(students):
    passed = 0
    for s in students:
        if s["math"] >= 40 and s["reading"] >= 40 and s["writing"] >= 40:
            passed += 1
    print(passed, "out of", len(students), "passed all subjects")


students = clean_data(read_data("StudentsPerformance.csv"))
print("Total students:", len(students))

print("\nSubject scores")
subject_stats(students)

print("\nAverage by gender")
average_by(students, "gender")

print("\nAverage by test prep")
average_by(students, "prep")

print("\nAverage by lunch")
average_by(students, "lunch")

print("\nPass count")
pass_count(students)
