# Logical operators and conditional statements

A = int(input("A:"))
G = input("M/F:")
if ((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif ((A == 3 or A == 4) and G == "F"):
    print("fee is 200")
elif ((A == 5) and G == "M"):
    print("fee is 300")
else:
    print("no fee")
    

#Output:
'''
A:5
G:M
fee is 300

A:2
G:M
fee is 100
'''

#Single line if/Ternary operator
'''<var>=val1 if condition else val2'''

food =input("Food:")
eat ="Yes" if food == "Pizza" else "No"
print(eat)

food= input("Food: ")
print("sweet") if food == "Jalebi" else print("not sweet")

#clever if/ Ternary operator
'''<var>=(false_val, true_val)[condition]'''

age = int(input("Enter your age:"))
vote = ("yes", "no")[age >= 18]
if (age <=18):
    print("you cannot vote")
else:
    print("You can vote")

sal = float (input("Enter your  salary:"))
tax = (sal*0.1, sal*0.2)[sal <= 50000]
if (sal <= 50000):
    print(tax)
else:
    print("No tax is calculated")


