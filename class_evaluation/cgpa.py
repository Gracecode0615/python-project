"""Problem Statement
Write a software to calculate the a semester Grade Point (GP) of Student of Lagos State University(LASU) in faculty of science. 
All student of the faculty are to offer the following 10 courses, each courses having their unit. 

Course Code     Unit
FOS101          3 Units
FOS102          4 Units
FOS103          3 Units
FOS104          4 Units
FOS105          3 Units
FOS106          4 Units
FOS107          3 Units
FOS108          4 Units
FOS109          3 Units
FOS110          4 Units

They are to provide the following Data
1. Name 
2. Matric No 
3. Department 
4. Level
5. Course score
"""
# collecting data from student
print("Welcome to the Faculty of Science, This is a program that helps student calculates CPGA for each semester  ")
student_name = input("Enter your name ")
matric_no = int(input(f"Dear {student_name}, Kindly enter your Matric no: "))
department = input("Enter your Department: ")
level = input("Enter your level ")
print(f"The following Data provided by {student_name} in {level}l with the matric no - {matric_no} in the department of {department} ")



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
# initializing
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


# Collecting student scores for each course
student_scores = {}
for course in ["FOS101", "FOS102", "FOS103", "FOS104", "FOS105", "FOS106", "FOS107", "FOS108", "FOS109", "FOS110"]:
    score = int(input("Enter score for {}: ".format(course)))
    student_scores[course] = score

# Calculating the GPA
gpa = calculate_semester_gpa(student_scores)


# Printing the results
print("\nStudent Name:", student_name)
print("Matric No:", matric_no)
print("Department:", department)
print("Level:", level)


print("Semester GPA:", round(gpa, 2))  # Rounding GPA to 2 decimal places
