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



print("Welcome to the Faculty of Science, This is a program that helps student calculates CPGA for each semester  ")
student_name = input("Enter your name ")
matric_no = int(input(f"Dear {student_name}, Kindly enter your Matric no: "))
department = input("Enter your Department: ")
level = input("Enter your level ")
print(f"The following Data provided by {student_name} in {level}l with the matric no - {matric_no} in the department of {department} ")
 
grade = int(input("Enter your score "))
FOS_101 = int("5")
FOS_102 = int("3")
FOS_103 = int("4")
FOS_104 = int("3")
FOS_105 = int("3")
FOS_106 = int("2")
FOS_107 = int("4")
FOS_108 = int("2")
FOS_109 = int("3")
FOS_110 = int("4")

unit = float(input(f""))

