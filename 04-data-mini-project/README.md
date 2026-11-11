# Student Performance Analysis
Reads a CSV of student exam scores and prints some statistics.

Dataset: [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) (Kaggle)

## How it works

- `read_data()` reads the CSV
- `clean_data()` skips empty rows, converts scores to numbers and adds an average
- `subject_stats()`, `average_by()` and `pass_count()` calculate the stats using numpy

## Stats

1. average, max and min for each subject
2. average by gender
3. average by test prep course
4. average by lunch type
5. students who passed all subjects (40+)

## How to run

```
pip install numpy
cd 04-data-mini-project
python main.py
```

## Results

- test prep course: 72.7 vs 65.0 without it
- standard lunch: 70.8 vs 62.2 for free/reduced
- female 69.6, male 65.8
- 949 out of 1000 passed all subjects

**I used an AI assistant to help with parts of the code.**
