'''LOOPS'''

#TYPES OF LOOPS
# for loop
# while loop

'''range(5)'''
# start=0
# end=4
# increment=1
# 1,2,3,4

'''range(1,10)'''
# start=1
# end=9
# increment=1
# 1,2,3,4

'''range(5,10,3)'''
# start=5
# end=9
# increment=3
# 1,4,7,10

'''FOR LOOP'''
for a in range (5):
    print(a)
print()
for a in range (1,11,1):
    print("2*",a,"=",2*a)

'''REVERSE LOOP'''
range(10,1,-1)
start=10
end=2
decrement=-1

for a in range(10,2,-1):
    print(a)

'''WHILE LOOP'''
i=1
while i<=10:
    print(i,"I am learning python")
    i=i+1

print(i)

'''REVERSE WHILE LOOP'''
a=10
while a>=1:
    print(a,"hello")
    a=a-1

