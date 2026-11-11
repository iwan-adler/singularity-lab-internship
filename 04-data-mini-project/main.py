import csv
import numpy as np

FILE_NAME = "StudentsPerformance.csv"
PASS_MARK = 40


# read the csv file and return a list of rows (each row is a dictionary)
def read_data(file_name):
    rows = []
    with open(file_name, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


# clean the data: remove rows with missing values and change scores to numbers
def clean_data(rows):
    clean_rows = []
    for row in rows:
        try:
            student = {
                "gender": row["gender"].strip(),
                "lunch": row["lunch"].strip(),
                "test_prep": row["test preparation course"].strip(),
                "math": int(row["math score"]),
                "reading": int(row["reading score"]),
                "writing": int(row["writing score"]),
            }
        except (ValueError, KeyError):
            continue  # skip bad rows

        # add an average score for each student
        student["average"] = round((student["math"] + student["reading"] + student["writing"]) / 3, 2)
        clean_rows.append(student)
    return clean_rows


# get all the values of one column as a numpy array
def get_column(students, column):
    values = []
    for s in students:
        values.append(s[column])
    return np.array(values)


# 1. average, highest and lowest score for each subject
def subject_stats(students):
    print("1. Subject scores")
    for subject in ["math", "reading", "writing"]:
        scores = get_column(students, subject)
        print(f"   {subject}: average = {np.mean(scores):.2f}, highest = {np.max(scores)}, lowest = {np.min(scores)}")


# 2. average score by gender
def average_by_gender(students):
    print("2. Average score by gender")
    groups = {}
    for s in students:
        if s["gender"] not in groups:
            groups[s["gender"]] = []
        groups[s["gender"]].append(s["average"])
    for gender, scores in groups.items():
        print(f"   {gender}: {np.mean(scores):.2f}")


# 3. does the test preparation course help?
def test_prep_effect(students):
    print("3. Test preparation course")
    completed = []
    not_completed = []
    for s in students:
        if s["test_prep"] == "completed":
            completed.append(s["average"])
        else:
            not_completed.append(s["average"])
    print(f"   completed: {np.mean(completed):.2f} ({len(completed)} students)")
    print(f"   not completed: {np.mean(not_completed):.2f} ({len(not_completed)} students)")


# 4. does lunch type affect scores?
def lunch_effect(students):
    print("4. Average score by lunch type")
    groups = {}
    for s in students:
        if s["lunch"] not in groups:
            groups[s["lunch"]] = []
        groups[s["lunch"]].append(s["average"])
    for lunch, scores in groups.items():
        print(f"   {lunch}: {np.mean(scores):.2f}")


# 5. how many students passed all three subjects
def pass_count(students):
    passed = 0
    for s in students:
        if s["math"] >= PASS_MARK and s["reading"] >= PASS_MARK and s["writing"] >= PASS_MARK:
            passed += 1
    percent = passed / len(students) * 100
    print("5. Students who passed all subjects (40 or more)")
    print(f"   {passed} out of {len(students)} ({percent:.1f}%)")


# 6. top 5 students by average score
def top_students(students):
    print("6. Top 5 average scores")
    sorted_students = sorted(students, key=lambda s: s["average"], reverse=True)
    for i in range(5):
        s = sorted_students[i]
        print(f"   {i + 1}. {s['gender']} - {s['average']}")


def main():
    rows = read_data(FILE_NAME)
    students = clean_data(rows)
    print(f"Loaded {len(rows)} rows, {len(students)} after cleaning\n")

    subject_stats(students)
    average_by_gender(students)
    test_prep_effect(students)
    lunch_effect(students)
    pass_count(students)
    top_students(students)


main()
