num = 2
for a in range(1,300):
    print(num * a)

one = 1
for b in range (3,30,3):
    print(one * a)


sum = 0
for n in range(1,11):
    sum += n
    print(sum)



for i in range(1,11):
    for j in range (1, i+1):
        print(i, end="")
        print(i)
        '''
        Outer loop (for i in range(1, 11)): This loop runs from 1 to 10, iterating through each number i.
        Inner loop (for j in range(1, i + 1)): For each i, this loop runs from 1 to i, printing the number i i times on the same line.
        print(i, end=""): This prints the number i without moving to a new line.
        print(): This moves to the next line after the inner loop has completed for the current i.

        '''

        # calculate the 5th multiplication from 5x1 =5 to 5 x 50 sing loop 

# Loop from 1 to 50
for i in range(1, 51):
    # Calculate the multiplication result
    result = 5 * i
    # Print the multiplication result
    print(f"5 x {i} = {result}")
    # Highlight the 5th multiplication
    if i == 5:
        print(f"--> The 5th multiplication is: 5 x {i} = {result}")

for i in range (0,10):
    print(i)

# nested for loop
for i in range (1,10):
    for j in range(9, i-1, -1):
        print("*", end= "")
    print("*")
    '''
        Outer loop (for i in range(1, 10)): This loop runs from 1 to 9.
        Inner loop (for j in range(9, i - 1, -1)): This loop starts from 9 and decrements j until it reaches i-1.
        This controls the number of asterisks printed on each line.
        print("*", end=""): This prints an asterisk without moving to a new line.
        print(): This moves to the next line after printing the required number of asterisks for the current line.
    '''

nom = 3
for n in range(2,10):
    nom += n
    print(nom)


# while loop
'''
syntax 
while[a condition is True]:
....body 1, do something
....body 2, do something
....body 3, do something
'''
a = 10
while a > 0:
    print(f"value of a is {a}")
    a -= 2 
    # a=a-2
print("loop is completed")