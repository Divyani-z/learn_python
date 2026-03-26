'''CONDITIONAL STATEMENTS'''
#types of conditional statement
# 1.if statement
# 2.if else statement
# 3.if elif else statement 

'''IF STATEMENT'''
# To print Even number

a=int(input("Enter the value:"))
if a % 2 == 0:
    print (a, "is Even Number")
 
'''IF ELSE STATEMENT'''
#To print Even Odd number 

a=int(input("Enter the value:"))
if a % 2 == 0:
    print (a, "is Even Number")
else:
    print (a, " is Odd Number")
 
'''IF ELIF ELSE STATEMENT'''
#To print student rank

a= int(input("Enter the value: "))
if a>=90:
    print(a,"first rank")
elif a>=70:
    print(a,"second rank")
elif a>=60:
    print(a, "third rank")
else:
    print (a, "fail")

# Traffic light program 

light = input("Enter the traffic light color:")
if (light== "red"):
    print("stop")
elif (light== "yellow"):
    print("Wait")
elif(light== "green"):
    print("Go")
else:
    print("Light is broken")