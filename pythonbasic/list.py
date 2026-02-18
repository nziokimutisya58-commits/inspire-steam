# benedict musa
# 18/2/2026
# Program to show list in python

friends =  ["Rachel","Pheobe","Ross","Chandler","Joey","Monica"]

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)
friends.append("Jack")
print(friends)

new_friends = ["Mike","Antony","Earnest","James"]

print(len(new_friends))

#new list of students
Students = friends + new_friends 

print(Students)
Students.pop()
print(Students)
Students.insert(5,"Jenny")
print(Students)
Students.insert(9,"Joshua")
print(Students)
Students.extend("Dan")
print(Students)
Students.remove("Jack")
print(Students)

new_Students = Students.copy()
print(new_Students)
