# marks1 = 94.4
# marks2 = 87.4
# marks3 = 78.4
# marks4 = 67.3
# marks5 = 54.2

# marks = [94.4, 87.4, 78.4, 67.3, 54.2]
# print(marks)

# student =["karan", 98, "Pune"]
# student[0] = "Arjun"
# print(student[0])

# print(student[0:1])/


'''List methods'''

#append adds an element at the end 
list =[ 1,2,3,4,5,6,7,8,9,10]
print(list.append(11))

#sorting list in ascending order
print (list.sort(reverse=False))
print(list)

#sorting list in descending order
print(list.reverse())
print(list)

#inser element at a particular index
print(list.insert(0, 0))
print(list)

#removing element from list
print(list.remove(5))
print(list)

#removing element from a particular index
print(list.pop(0))
print(list)