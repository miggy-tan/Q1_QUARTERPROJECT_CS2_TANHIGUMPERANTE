# __[STUDYPULSE: Grade and Wellness Tracker]__
##### By Miguel Tan, Nobi Higum, and Jace Perante

##### Jace pls add to this text its still a draft, i did some parts tho, and im sleepy 🥱 goodnight jac-

##### This program calculates the required grade to get to the target grade (inputted). It also calculates the study hours depending on which difficulty you choose.

# Features
##### [not yet done]

# Requirements
- Python 3

# Inputs Needed
* Subject Name
* Subject Grade
* Target Grade
* Difficulty (1-5) with 5 being the highest
* Days Left until Exam

# Outputs
https://github.com/user-attachments/assets/c96323ec-de14-4615-99ed-acabb3be0890

# Calculations

```text
def calculate_exam_score(current_grade, target_grade, exam_weight):
    current_weight = 1.0 - (exam_weight / 100.0)
    earned_points = current_grade * current_weight
    needed_points = target_grade - earned_points
    return round(needed_points / (exam_weight / 100.0), 2)
```
