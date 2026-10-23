
# __[STUDYPULSE: Target Grade Calculator]__
##### By Miguel Tan, Nobi Higum, and Jace Perante

##### StudyPulse is a simple tool designed to take the stress out of exam prep. Instead of guessing what you need to pass, you just type in your current grade, your goal grade, and how much your test is worth. The program calculates the exact score you need on your exam so you can plan ahead with confidence.

## Problem Statement
##### Problem Statement
##### Many students feel anxious before big exams because they do not know what score they actually need to hit their goal grade. According to research on goal-setting theory and self-efficacy by [Locke & Latham (2002)](https://doi.org/10.1037/0003-066X.57.9.705) and [Schunk (1990)](https://doi.org/10.1207/s15326985ep2501_6), setting clear and specific academic targets significantly lowers test anxiety, builds confidence, and helps students focus better on their work. StudyPulse solves this by giving students quick, clear math on their required exam score so they know exactly what to aim for.

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
https://github.com/user-attachments/assets/faf821f3-8dac-4861-9e8d-dbbef5051429



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

## Contributors
* Nobi Higum: Core logic & Workflow
* Miguel Tan: Input validation
* Jace Perante: Flowchart
