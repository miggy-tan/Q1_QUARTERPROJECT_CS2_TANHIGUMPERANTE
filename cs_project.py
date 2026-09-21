# CS Project
# Full Code
# by Miguel Tan and Nobi Higum

import os

RED = "\033[31m"
LIGHT_RED = "\033[1;31m"
WHITE = "\033[37m"
GREEN = "\033[32m"
CYAN = "\033[36m"
RESET = "\033[0m"

def user_inputs():
    while True:
        subject = input("Enter Subject Name: ").strip()
        if not subject:
            print(f"{RED}Error: No input provided for subject name.{RESET}")
            continue
        break

    while True:
        try:
            current_grade_input = input("Enter Current Grade (%): ").strip()
            if not current_grade_input:
                print(f"{RED}Error: No input provided for current grade.{RESET}")
                continue
            current_grade = float(current_grade_input)
            if not (0 <= current_grade <= 100):
                print(f"{RED}Error: Current grade must be between 0 and 100.{RESET}")
                continue
            break
        except ValueError:
            print(f"{RED}Error: Input a number for current grade.{RESET}")

    while True:
        try:
            target_grade_input = input("Enter Target Grade (%): ").strip()
            if not target_grade_input:
                print(f"{RED}Error: No input provided for target grade.{RESET}")
                continue
            target_grade = float(target_grade_input)
            if not (0 <= target_grade <= 100):
                print(f"{RED}Error: Target grade must be between 0 and 100.{RESET}")
                continue
            break
        except ValueError:
            print(f"{RED}Error: Input a number for target grade.{RESET}")

    while True:
        try:
            exam_weight_input = input("Enter Remaining Exam Weight (%): ").strip()
            if not exam_weight_input:
                print(f"{RED}Error: No input provided for exam weight.{RESET}")
                continue
            exam_weight = float(exam_weight_input)
            if not (0 < exam_weight <= 100):
                print(f"{RED}Error: Exam weight must be greater than 0 and no more than 100.{RESET}")
                continue
            break
        except ValueError:
            print(f"{RED}Error: Input a number for exam weight.{RESET}")

    while True:
        try:
            difficulty_input = input("Enter Difficulty Level (1-5): ").strip()
            if not difficulty_input:
                print(f"{RED}Error: No input provided for difficulty level.{RESET}")
                continue
            difficulty = int(difficulty_input)
            if not (1 <= difficulty <= 5):
                print(f"{RED}Error: Difficulty level must be between 1 and 5.{RESET}")
                continue
            break
        except ValueError:
            print(f"{RED}Error: Input a whole number for difficulty level.{RESET}")

    while True:
        try:
            days_left_input = input("Enter Days Left Until Exam: ").strip()
            if not days_left_input:
                print(f"{RED}Error: No input provided for days left.{RESET}")
                continue
            days_left = int(days_left_input)
            if days_left < 0:
                print(f"{RED}Error: Days left cannot be negative.{RESET}")
                continue
            break
        except ValueError:
            print(f"{RED}Error: Input a whole number for days left.{RESET}")

    return {
        "subject": subject,
        "current_grade": current_grade,
        "target_grade": target_grade,
        "exam_weight": exam_weight,
        "difficulty": difficulty,
        "days_left": days_left
    }

def calculate_exam_score(current_grade, target_grade, exam_weight):
    current_weight = 1.0 - (exam_weight / 100.0)
    earned_points = current_grade * current_weight
    needed_points = target_grade - earned_points
    return round(needed_points / (exam_weight / 100.0), 2)

def workload_and_health(difficulty, days_left, min_score):
    daily_study_time = round(1.0 + (difficulty * 0.35) + max(0, (5 - days_left) * 0.1), 1)

    if daily_study_time >= 3.0 or (difficulty >= 4 and days_left <= 3):
        burnout_risk = "HIGH"
    elif daily_study_time >= 2.0:
        burnout_risk = "MODERATE"
    else:
        burnout_risk = "LOW"

    return {
        "daily_study_time": daily_study_time,
        "burnout_risk": burnout_risk,
        "is_achievable": 0.0 <= min_score <= 100.0,
        "already_secured": min_score < 0.0
    }

def print_results(min_score, analysis):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--------------------------------------------------")
    print("[RESULTS & PREDICTIONS]")

    if analysis["already_secured"]:
        print(f"- Target Status: {GREEN}ALREADY SECURED{RESET}\n")
        print(f"{GREEN}You've already reached your target grade based on your current grade alone!")
        print(f"You could score 0% on the exam and still hit your target.{RESET}")
    else:
        status = "ACHIEVABLE" if analysis["is_achievable"] else "UNACHIEVABLE"
        print(f"- Target Status: {status}")
        print(f"- Minimum Score Needed on Exam: {min_score}%")

        if not analysis["is_achievable"]:
            print("\nHEALTH-CHECK WARNING")
            print(f"{RED}To reach your target grade, you need an impossible score on the exam!{RESET}")
            print("Consider adjusting your target grade to a realistic goal.")

    print(f"\nRecommended Daily Study Time: {analysis['daily_study_time']} hours/day")
    print(f"Burnout Risk: {analysis['burnout_risk']} – Don't forget to take breaks!")
    print("--------------------------------------------------")

def print_authors():
    print("Authors:")
    print(f"- {CYAN}Nobi Higum{RESET} – Grade Target Calculator & Core Logic")
    print(f"- {CYAN}Miguel Tan{RESET} – Workload Estimator & Input Validation")
    print(f"- {CYAN}Jace Perante{RESET} – Project Setup & Technical Documentation")
    print(f"- {LIGHT_RED}Section:{RESET} 8-Camia")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{WHITE}|================================================|{RESET}")
    print(f"{WHITE}        STUDYPULSE: GRADE & WELLNESS TRACKER      {RESET}")
    print(f"{WHITE}|================================================|{RESET}")

    data = user_inputs()

    min_score = calculate_exam_score(
        data["current_grade"],
        data["target_grade"],
        data["exam_weight"]
    )

    analysis = workload_and_health(
        data["difficulty"],
        data["days_left"],
        min_score
    )

    print_results(min_score, analysis)
    input("Press Enter to continue: ")

    print("\n========================================\n")
    print_authors()

if __name__ == "__main__":
    main()
