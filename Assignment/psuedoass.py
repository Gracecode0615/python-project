# this program wants to calculate the value of G, if G = gk/sl

print("welcome to this calulation")
valueg = input("Enter the value of g? ")
valuek = input("Enter the value of k? ")
values = input("Enter the value of s? ")
valuel = input("Enter the value of l? ")
intofg = int(valueg)
intofk = int(valuek)
intofs = int(values)
intofl = int(valuel)
valueofUF = intofg * intofk 
valueofLF = intofs * intofl
valueofAF = valueofUF / valueofLF
print("the value of G " + str(valueofAF))
