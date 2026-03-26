#  Input statements

Name = input("Enter your name:")
print ("Hello", Name)
print("What is your age?")
age = int(input("Enter your age:"))
print("your age is", age)

# Write a program to input 2 numbers and print their sum.

num1 = int (input("Enter the first number:"))
num2 = int (input("Enter the second number:"))
sum = num1 + num2
print("The sum of the two numbers is:", sum)

# WAP to input 2 floating numbers and print their average.

first = float (input("Enter first number:"))
second = float (input("Enter second number:"))
average = (first + second) / 2
print("The average of the two numbers is:", average)

# WAP to input 2 int numbers, a and b. print true if a is greater than or equal to b . if not print false.

a = int (input("Enter the value of a:"))
b = int (input("Enter the value of b:"))
if(a >= b):
    print("True")
else:
    print("False")
