
# __[STUDYPULSE: Target Grade Calculator]__
##### By Miguel Tan, Nobi Higum, and Jace Perante

##### StudyPulse is a simple tool designed to take the stress out of exam prep. Instead of guessing what you need to pass, you just type in your current grade, your goal grade, and how much your test is worth. The program calculates the exact score you need on your exam so you can plan ahead with confidence.

## Features
- Required Exam Grade Calculator: Figures out the grade you need on your upcoming test using your current grade, goal grade, and test weight.
- Reality Check Alerts: Displays a warning if your target grade requires a score above 100% or below 0%.
- Simple Terminal Menu: Guides you step-by-step through clear command-line prompts.

## Requirements
- Python 3

## How to run:
Input the following values
- Subject Name
- Current Subject Grade (%)
- Target Final Grade (%)
- Exam Weight (%)

## Outputs to expect:
https://github.com/user-attachments/assets/faf821f3-8dac-4861-9e8d-dbbef5051429

## Calculations

```text
def calculate_exam_score(current_grade, target_grade, exam_weight):
    current_weight = 1.0 - (exam_weight / 100.0)
    earned_points = current_grade * current_weight
    needed_points = target_grade - earned_points
    return round(needed_points / (exam_weight / 100.0), 2)
```

## Contributors
* Nobi Higum: Core logic & Workflow
* Miguel Tan: Input validation
* Jace Perante: Flowchart
