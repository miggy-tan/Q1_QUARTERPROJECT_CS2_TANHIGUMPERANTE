
# __[STUDYPULSE: Target Grade Calculator]__
##### By Miguel Tan, Nobi Higum, and Jace Perante

##### StudyPulse is a simple tool designed to take the stress out of exam prep. Instead of guessing what you need to pass, you just type in your current grade, your goal grade, and how much your test is worth. The program calculates the exact score you need on your exam so you can plan ahead with confidence.

## Problem Statement
##### Many students feel anxious before big exams because they do not know what score they actually need to hit their goal grade. Research shows that having clear, specific academic targets lowers study stress and helps students focus better. StudyPulse solves this by giving students quick, clear math on their required exam score so they know exactly what to aim for.

## Project Objectives
- Find Required Exam Grades: Calculate the exact score needed on an upcoming exam to reach a final target grade.
- Catch Impossible Goals: Warn students right away if a target grade requires an impossible test score (like over 100%).

## Features
- Required Exam Grade Calculator: Figures out the grade you need on your upcoming test using your current grade, goal grade, and test weight.
- Reality Check Alerts: Displays a warning if your target grade requires a score above 100% or below 0%.
- Simple Terminal Menu: Guides you step-by-step through clear command-line prompts.

## Requirements
- Python 3

## Inputs Needed
- Subject Name
- Current Subject Grade (%)
- Target Final Grade (%)
- Exam Weight (%)

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
#### by Jace Perante
<img width="750" height="833" alt="image" src="https://github.com/user-attachments/assets/988faa62-73cf-4aa5-9057-181c33bbee8c" /> 

## Contributors
* Nobi Higum: Core logic & Workflow
* Miguel Tan: Input validation
* Jace Perante: Flowchart
