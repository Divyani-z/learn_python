'''LOOPS IN PYTHON'''

'''SYNTAX'''
# outer_loop:
#   inner_loop:
        # bolck of code for inner loop
# block of code for outer loop

'''EXAMPLE 1'''
# print numbers from 1 to 3

for i in range(3):
    print ("Outer loop iteration no.",i)
    for num in range(1,4):
     print (num)
    print("---")

'''EXAMPLE 2'''
# print numbers 1 to 4 
# using while-for loop

i=1
while i<4:
  for n in range(1,2):
    print(i,"DIVYANI")  
  print("---")
  i=i+1
  for n in range(1,3):
    print(i,"DIVYANI")  
  print("---")
  i=i+1
  for n in range(1,4):
    print(i,"DIVYANI")  
  print("---")
  i=i+1
  for n in range(1,5):
    print(i,"DIVYANI")  
  print("---")
  i=i+1
print("end")

'''EXAMPLE 3'''
# print prime numbers between 2 to 10 using nested loop

for num in range (2,10):
    for i in range(2,num):
        if num % i == 0:
         break    
    else:
      print(num)



