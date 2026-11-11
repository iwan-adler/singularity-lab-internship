# Student Performance Analysis

A simple Python program that reads a CSV file of student exam scores and prints some statistics.

Dataset: [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) from Kaggle (1000 students, math / reading / writing scores).

## How it works

1. `read_data()` reads the CSV file using the `csv` module and stores each row as a dictionary
2. `clean_data()` changes the scores to numbers, skips bad rows and adds an average score for each student
3. the other functions calculate the statistics using loops, lists, dictionaries and numpy

## Statistics

1. average, highest and lowest score for each subject
2. average score by gender
3. test preparation course vs no course
4. average score by lunch type
5. number of students who passed all subjects (40 or more)
6. top 5 students by average score

## How to run

You need Python and numpy.

```
pip install numpy
cd 04-data-mini-project
python main.py
```

## What I found

- students who completed the test preparation course scored about 7.6 marks higher on average
- students with standard lunch scored about 8.6 marks higher than free/reduced lunch
- female students had a higher average (69.6) than male students (65.8)
- 94.9% of students passed all three subjects

---

I used an AI assistant to help with parts of the code.
