
# __[STUDYPULSE: Grade and Wellness Tracker]__
##### By Miguel Tan, Nobi Higum, and Jace Perante

##### This program calculates the required grade to get to the target grade (inputted). It also calculates the study hours depending on which difficulty you choose. StudyPulse helps you plan ahead for exams without the guesswork. You just type in your current grades and test dates, and it calculates what score you need to pass or reach your goal. It also gives you a daily study schedule based on how hard the subject is.

## Features
* Required Exam Grade Calculator: Figures out what grade you need on your upcoming test based on your current grade, your goal grade, and how much the test is worth.
* Study Time Estimator: Works out how many total and daily hours you should study by looking at how hard you rated the subject (1 to 5) and how many days you have left.
* Simple Screen Menu: Prompts you step-by-step in the terminal to enter your information and displays your results clearly.
* Reality Check Alerts: Gives you a heads-up if your target grade requires an impossible score (like needing over 100% on a test) or if the suggested study hours are too high for one day.
* Multi-Subject Tracker: Lets you enter information for several classes in one go so you can see which subject needs your attention most.

## Requirements
- Python 3

## Inputs Needed
* Subject Name
* Subject Grade
* Target Grade
* Difficulty (1-5) with 5 being the highest
* Days Left until Exam

## Outputs
https://github.com/user-attachments/assets/c96323ec-de14-4615-99ed-acabb3be0890

## Calculations

```text
def calculate_exam_score(current_grade, target_grade, exam_weight):
    current_weight = 1.0 - (exam_weight / 100.0)
    earned_points = current_grade * current_weight
    needed_points = target_grade - earned_points
    return round(needed_points / (exam_weight / 100.0), 2)
```
## LOGIC PLAN( FLOWCHART )
#### by Jace Perante (ai-generated image)
<img width="750" height="833" alt="image" src="https://github.com/user-attachments/assets/988faa62-73cf-4aa5-9057-181c33bbee8c" /> 

