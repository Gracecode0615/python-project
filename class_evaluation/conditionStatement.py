"""
write a script to handle user's age and print their category
0 - 2 = infant
3 - 11 kid
12 -19 = teenager
20 -34 = young Adult
35 -69 = Adult
70 - 99 = Old man
"""
print("Dear User, Welcome to this program")
age = input("Enter your Age: ")
age = int(age)
if 0 <= age <= 2:
        print("You belong to an Infant Catergory")
elif 3 <= age <= 11:
 print("You belong to a kid Catergory")
elif 12 <= age <= 19:
        print(" You belong to a Teenager Catergory")
elif 20 <= age <= 34:
        print("You belong to a Young Adult Catergory")
elif 35 <= age <= 69:
        print("You belong to an Adult Catergory")
elif 70 <= age <= 99:
        print("You belong to an Aged Catergory")
else:
        print("Thank you for checking")



# name = input("enter your age")
# if age == 40
# print (f"Yez, your age is {age}")
# else if 
# print(f"you're still young") 

# age = input("Enter your age: ")
# try:
#     age = int(age)  # Convert the input to an integer
#     if age == 40:
#         print(f"Yes, your age is {age}")
#     else:
#         print("You're still young")
# except ValueError:
#     print("Please enter a valid number for your age")



# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')


# Age = input ("Kindly enter your age?\n")
#     if Age <= 11 or Age >= 3:
#     print("You're a Kid!")
# else if Age <= 19 or Age >= 12:
#     print("You're a teenager")
 