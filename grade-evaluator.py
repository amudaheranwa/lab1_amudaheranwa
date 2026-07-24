import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # a) Grade Validation
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"Error: '{item['assignment']}' has an invalid score ({item['score']}).")
            sys.exit(1)

    # b) Weight Validation
    total_weight = 0
    summative_weight = 0
    formative_weight = 0

    for item in data:
        total_weight += item['weight']
        if item['group'] == 'Summative':
            summative_weight += item['weight']
        elif item['group'] == 'Formative':
            formative_weight += item['weight']

    if total_weight != 100:
        print(f"Error: Total weight is {total_weight}, expected 100.")
        sys.exit(1)
    if summative_weight != 40:
        print(f"Error: Summative weight is {summative_weight}, expected 40.")
        sys.exit(1)
    if formative_weight != 60:
        print(f"Error: Formative weight is {formative_weight}, expected 60.")
        sys.exit(1)

    # c) GPA Calculation
    summative_total = 0
    formative_total = 0

    for item in data:
        weighted_score = item['score'] * item['weight'] / 100
        if item['group'] == 'Summative':
            summative_total += weighted_score
        elif item['group'] == 'Formative':
            formative_total += weighted_score

    final_grade = summative_total + formative_total
    gpa = (final_grade / 100) * 5.0

    # d) Pass/Fail (needs >= 50% in EACH category, not just overall)
    summative_percent = (summative_total / summative_weight) * 100
    formative_percent = (formative_total / formative_weight) * 100

    passed = summative_percent >= 50 and formative_percent >= 50

    # e) Resubmission Logic
    failed_formatives = []
    for item in data:
        if item['group'] == 'Formative' and item['score'] < 50:
            failed_formatives.append(item)

    resubmission_list = []
    if failed_formatives:
        highest_weight = 0
        for item in failed_formatives:
            if item['weight'] > highest_weight:
                highest_weight = item['weight']

        for item in failed_formatives:
            if item['weight'] == highest_weight:
                resubmission_list.append(item['assignment'])

    # f) Print the final decision and resubmission options
    print(f"Summative Score: {summative_percent:.2f}%")
    print(f"Formative Score: {formative_percent:.2f}%")
    print(f"Final Grade: {final_grade:.2f}%")
    print(f"GPA: {gpa:.2f}")

    if passed:
        print("Final Status: PASSED")
    else:
        print("Final Status: FAILED")

    if resubmission_list:
        print("Eligible for resubmission:")
        for assignment in resubmission_list:
            print(f"- {assignment}")
    else:
        print("No resubmission needed.")

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)