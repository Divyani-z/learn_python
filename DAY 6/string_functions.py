#string functions

#'''1.endswith()-returns True if string endswith substr'''

str="I am learning python from ApnaCollege"
print(str.endswith("ege"))

#'''2.captalize()-capital first letter'''

str = "i am going out today" 
print(str.capitalize())
 
str = "i am ready" 
str=(str.capitalize())
print(str)


#'''3.replace()- replaces old occurrence with new occurence '''

a = "Hey i am Software Developer"
a = (a.replace("Software", "Python"))
print(a)

#'''4.find()- returns the index of the first occurrence of the substring'''

str = "I am learning Python"
print(str.find("Python"))

#'''5.Count()- returns the number of occurrences of a substring'''

str = "I am learning Python and I am learning Java"
print(str.count("learning"))