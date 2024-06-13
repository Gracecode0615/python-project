def calculate_gp(score):
    if 70 <= score <= 100:
        return 5
    elif 60 <= score <= 69:
        return 4
    elif 50 <= score <= 59:
        return 3
    elif 45 <= score <= 49:
        return 2
    elif 40 <= score <= 44:
        return 1
    elif 0 <= score <= 39:
        return 0
    else:
        return 0

def calculate_semester_gpa(student_scores):
    courses = {
        "FOS101": 3,
        "FOS102": 4,
        "FOS103": 3,
        "FOS104": 4,
        "FOS105": 3,
        "FOS106": 4,
        "FOS107": 3,
        "FOS108": 4,
        "FOS109": 3,
        "FOS110": 4
    }

    total_units = 0
    total_weighted_gp = 0

    for course, score in student_scores.items():
        unit = courses[course]
        gp = calculate_gp(score)
        weighted_gp = gp * unit
        total_units += unit
        total_weighted_gp += weighted_gp

    gpa = total_weighted_gp / total_units
    return gpa

# Collecting student data
student_name = input("Enter student name: ")
student_matric = input("Enter matric number: ")
student_department = input("Enter department: ")
student_level = input("Enter level: ")

# Collecting student scores for each course
student_scores = {}
for course in ["FOS101", "FOS102", "FOS103", "FOS104", "FOS105", "FOS106", "FOS107", "FOS108", "FOS109", "FOS110"]:
    score = int(input("Enter score for {}: ".format(course)))
    student_scores[course] = score

# Calculating the GPA
gpa = calculate_semester_gpa(student_scores)

# Printing the results
print("\nStudent Name:", student_name)
print("Matric No:", student_matric)
print("Department:", student_department)
print("Level:", student_level)
print("Semester GPA:", round(gpa, 2))  # Rounding GPA to 2 decimal places
