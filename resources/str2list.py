#! /usr/bin/env python3

# take in a string, turn it into a list, modify the list and print it out

# declare a variable 'str' set to a string of last names
str = "Amin, Harris, Stites,"

# declare a variable that takes in a list of the string names
lst = str.split()
#print(lst)

# add first names at appropriate indexes
lst.insert(1, 'Neel')
#print(lst)
lst.insert(3, 'Alex')
#print(lst)
lst.insert(5, 'Greg')
#print(lst)
# print out the list in a column
print(lst[0], lst[1])
print(lst[2], lst[3])
print(lst[4], lst[5])
