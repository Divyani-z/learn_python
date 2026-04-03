# Function to add two numbers
def add(a, b):
    return a + b

# Function to greet user
def greet(name):
    print("Hello,", name)

# Main program
greet("Divyani")          # calling greet function
result = add(5, 3)        # calling add function
print("Sum is:", result)

#Factorial using function
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not possible")
else:
    result = factorial(num)
    print("Factorial is:", result)

#Check if number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("It is a Prime number")
else:
    print("Not a Prime number")