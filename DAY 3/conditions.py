'''CONDITIONAL STATEMENTS'''
#types of conditional statement
# 1.if statement
# 2.if else statement
# 3.if elif else statement 

#this is condition


'''IF STATEMENT'''
a=int(input("Enter the value:"))
if a % 2 == 0:
    print (a, "is Even Number")
 
'''IF ELSE STATEMENT'''
a=int(input("Enter the value:"))
if a % 2 == 0:
    print (a, "is Even Number")
else:
    print (a, " is Odd Number")
 
'''IF ELIF ELSE STATEMENT'''
a= int(input("Enter the value: "))
if a>=90:
    print(a,"first rank")
elif a>=70:
    print(a,"second rank")
elif a>=60:
    print(a, "third rank")
else:
    print (a, "fail")
