# write a script to evaluate students performance based on their grade
# 0-39 -- fair
# 40-44 --- poor
# 45 -49 --credit
# 50 - 59 ---good
# 60 -69 --- very good
# 70 -100 Excellent


print("Welcome, Chris")

grade = input("Enter your Grade ")
grade = int(grade)
if 0 <= grade <= 39:
    print("your cgpa is Fair")
elif 40 <= grade <= 44:
    print("Your fucking CGPA is Poor")
elif 41 <= grade <= 49:
    print("You tried, weldone your on a credit")
elif 50 <= grade <= 59:
    print("Your fucking CGPA is Good")
elif 60 <= grade <= 69:
    print("Your CGPA is very Good")
elif 70 <= grade <= 100:
    print("Congratulations!!! You are an Excellent Student")
else:
    print("it is invalid")
