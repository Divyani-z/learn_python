#WAP toask the user to enter names of thier 3 favourite movies and store them in a list.

movie =[]
mov1 = input("Enter 1st movie: ")
movie.append(mov1)
mov2 = input("Enter 2nd movie: ")
movie.append(mov2)
mov3 = input("Enter 3rd movie: ")
movie.append(mov3)
print(movie)

'''Another way to do same thing'''
movie =[]
movie.append(input("Enter 1st movie: "))
movie.append(input("Enter 2nd movie: "))
movie.append(input("Enter 3rd movie: "))
print(movie)

#WAP to check if the list is palindrome

list1 = [1, 2, 3, 2, 1]
copy_list = list.copy(list1)

list1.reverse()
print(list1)

if list1 == copy_list:
    print("Palindrome")
else:
    print("Not palindrome")

#WAP to count number of students with 'A' grade in the list od student grades
student_grade = ('C', 'D', 'A', 'A', 'B','B','A')
print(student_grade.count('A'))

student_grade = ['C', 'D', 'A', 'A', 'B','B','A']
student_grade.sort()
print(student_grade)
