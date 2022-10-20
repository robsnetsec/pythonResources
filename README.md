## Python Resources:  
     
      
## Template!
```python
#!/usr/bin/env python3
      
#function to do one specific task
def function1(string1):
    return(string1)
      
# main function to work in
def main():
    #I will do all my planning and executing
    #call our other function
    print(function1('hello!'))
#call our main function
if __name__ == '__main__':
    main()
```

## Weblinks for Learning


| Python websites                   | Weblinks                            |
| ------------------------------ | ---------------------------------- |
| Coursera - learn python | [📺][https://www.coursera.org/learn/python]
| Reddit - learn python | [📺][https://www.reddit.com/r/learnpython/]
| RealPython | [📺][https://realpython.com/]
| w3schools - python | [📺][https://www.w3schools.com/python/default.asp]
| Twilio - learn python | [📺][https://www.twilio.com/quest/learn/python]
| Python docs - built-in functions | [📺][https://docs.python.org/3/library/functions.html]      
| BinarySearch | [📺][https://binarysearch.com/]
| Leetcode | [📺][https://leetcode.com/explore/]
| YouTube vid 1 | [📺][https://www.youtube.com/watch?v=i5bFtbTbjzI]
| Youtube vid 2 | [📺][https://www.youtube.com/watch?v=ZH26PuX3re0]     
| Python3 Documentation | [📺][https://docs.python.org/3/]
| PBJ vid | [📺][https://www.youtube.com/watch?v=Ct-lOOUqmyY]
| 10 most useful Python String Methods | [📺][https://linuxhint.com/python_string_methods/] 
| Python 3 String Methods | [📺][https://www.python-ds.com/python-3-string-methods]
| Introduction to String Functions in Python 3 | [📺][https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3]      
| Python String Methods | [📺][https://www.programiz.com/python-programming/methods/string]
| Remove white spaces from Strings | [📺][https://www.journaldev.com/23763/python-remove-spaces-from-string]      
| Python List Methods | [📺][https://www.programiz.com/python-programming/methods/list] 
| Python Documentation - List Methods | [📺][https://docs.python.org/3/tutorial/datastructures.html] 
| Improving your python coding | [📺][https://www.codementor.io/blog/pythonic-code-6yxqdoktzt] 
| Improving your python coding 2 | [📺][https://techlog360.com/best-tools-improve-programming-coding-skills/]       
      
## Python Code Samples:      

| Topic                          | Links                            |
| ------------------------------ | ---------------------------------- |
| for loop over a string | [📝][prep1.py]
| input() method | [📝][prep2.py]
| modulus use | [📝][prep3.py]
| for loop with range function| [📝][prep4.py]
| for loop with range 2 | [📝][101.py]
| while loop w/ counter  | [📝][prep5.py]
| forever while loop | [📝][prep6.py]
| import random - if/elif/else | [📝][prep7.py]
| import random - while loop - if/else | [📝][prep8.py]
| import random - while loop - if/elif/break - if/else| [📝][prep9.py]
| enumerate() method - for loop| [📝][enumerate-function.pdf]      
| random password generator (simple)| [📝][randpass_simple.py]
| random password generator (better)| [📝][randpass_better.py]
| convert strings to lists / insert method for lists| [📝][str2list.py]      

[prep1.py]: resources/prep1.py
[prep2.py]: resources/prep2.py
[prep3.py]: resources/prep3.py
[prep4.py]: resources/prep4.py
[101.py]: resources/101.py
[prep5.py]: resources/prep5.py
[prep6.py]: resources/prep6.py
[prep7.py]: resources/prep7.py
[prep8.py]: resources/prep8.py
[prep9.py]: resources/prep9.py
[enumerate-function.pdf]: resources/enumerate-function.pdf      
[randpass_simple.py]: resources/randpass_simple.py
[randpass_better.py]: resources/randpass_better.py
[str2list.py]: resources/str2list.py   
          
      
# Python Functions

**Video link:** [https://youtu.be/-Bkupx9gX0o](https://youtu.be/-Bkupx9gX0o)

In this video, we learned about Python functions that make our program more organized and manageable by dividing our code into smaller and modular chunks.

---
## Python Functions
A function is a group of related statements that performs a specific task.

For example,

```python
def greet():
    print("Hello")
    print("How do you do?")
```
Here, we have defined a function named `greet`.

To create a function, we use the `def` keyword followed by the function name, parenthesis `()`, and a colon `:`.
The body of the function is specified using indentation.

When we run the program, we don't see any output.

It is because defining a function won't do anything. To bring the function into action, we need to call it.

```python
def greet():
    print("Hello")
    print("How do you do?")

greet()
```

**Output**

```
Hello
How do you do?
```

One advantage of defining a function is that we can call it any number of times.

```python
def greet():
    print("Hello")
    print("How do you do?")

greet()
greet()
greet()
```

**Output**

```
Hello
How do you do?
Hello
How do you do?
Hello
How do you do?
```

Also, we need to define a function first before we can call it.

The following code gives an error:

```python
# function call
greet()

# function definition
def greet():
    print("Hello")
    print("How do you do?")
```

When the `greet()` function is called, Python doesn't know that this function exists because it's defined after the function call.

---

## Function Arguments

Suppose we want to make our `greet()` function a bit more personal.

Instead of printing `Hello`, we want to print something like `Hello Jack` or whatever the person's name is.

For this, we can use function arguments:

```python
def greet(name):
    print("Hello", name)
    print("How do you do?")

greet("Jack")
```
**Output**

```
Hello Jack
How do you do?
```

Function arguments are passed inside the parenthesis during the function call.

It can then be accessed using the `name` parameter in the function definition.

---

## Passing Multiple Arguments

If we need to pass multiple arguments to a function, we can separate them by commas.

Let's create a function to add two numbers.

```python
def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is", result)


number1 = 5.4
number2 = 6.7
add_numbers(number1, number2)

```

**Output**

```
The sum is 12.100000000000001
```
We have passed `number1` and `number2` as arguments to the `add_numbers()` function.
These arguments are accepted as `n1` and `n2` once they are passed to the `add_numbers()` function.

>**Note:** We get this number instead of 12.1 because of floating-point representation error in Python.

---

## Return Value from Function

```python
def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is", result)


add_numbers(5.4, 6.7)
```
Sometimes it's better just to find the sum inside the function and print the result somewhere else.

We can achieve that by using the `return` statement.

```python
def add_numbers(n1, n2):
    result = n1 + n2
    return result

result = add_numbers(5.4, 6.7)
print("The sum is", result)
```

**Output**

```
The sum is 12.100000000000001
```

---
      
## Functions for opening files
      
```python
#!/usr/bin/env python3
import pprint
import sys
def simple(filename):
    # Open the file
    input_file = open(filename)
    # Read its contents
    contents = input_file.read()
    # Print out the contents
    pprint.pprint(contents)
    # close the file
    input_file.close()
def with_keyword(filename):
    # With this file open, do the following:
    with open(filename) as input_file:
        # read the contents.
        contents = input_file.read()
    # Later, print out the contents.
    pprint.pprint(contents)
def looping_files(filename):
    # With this filename opened as this variable, do the following:
    with open(filename) as input_file:
        # For each line in the file, do the following:
        for line in input_file:
            pprint.pprint('line = ' + line) # DEBUG
            # Remove the whitespace from the start and end of the string.
            line = line.strip()
            pprint.pprint('line = ' + line) # DEBUG
            # If 'nemo' is in the line, then
            if 'nemo' in line:
                # print the line.
                pprint.pprint(line)
def read_by_lines(filename):
    with open(filename) as input_file:
        contents = input_file.readlines()
    print(contents)
def main():
    # Get the filename from the first command line argument
    filename = sys.argv[1]
    print('=' * 50)
    print('simple method')
    simple(filename)
    print('=' * 50)
    print('using with keyword')
    with_keyword(filename)
    print('=' * 50)
    print('looping over a file')
    looping_files(filename)
    print('=' * 50)
if __name__ == '__main__':
    main()
``` 
    
---

## String Function samples
      
```python

#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
    if count >= 10:
        return "Number of donuts: many"
    else:
        return "Number of donuts: " + str(count)

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    if len(s) < 2:
         return ''
    else:
         return s[0:2] + s[-2] + s[-1]

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
  return s[0] + s[1:len(s)].replace(s[0], '*')

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  return str(b[0:2]) + str(a[2:len(a)]) + ' ' + str(a[0:2]) + str(b[2:len(b)])
  # return '{0}{1} {2}{3}'.format(b[0:2], a[2:len(a)], a[0:2], b[2:len(b)])

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  green = '\033[92m'
  red   = '\033[93m'
  end   = '\033[0m'

  if got == expected:
    prefix = green + 'OK' + end
  else:
    prefix = red + 'FAIL' + end
  print ' %s  got: %s expected: %s' % (prefix, repr(got), repr(expected))

# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print 'donuts'
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print
  print 'both_ends'
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  
  print
  print 'fix_start'
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print
  print 'mix_up'
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
```  
                  
---

## Dictionary samples
      
```python    
#!/usr/bin/env python3

ints = 1234567890
# print(ints, type(ints))
# print()
boolean = True
# print(boolean, type(boolean)) 
# print()
string = 'abcdaaaghghgh'
print(string, type(string))
print()
list1=['item1', 'item2', ['here is a list inside a list', 45],{'a':1, 'b':2}]
# print(list1, type(list1))
# print(list1[3], type(list1[3]))
# print()
dict2={}
dict1 = {'Alex':1, 'Greg': 2, string:list1}
# print(dict1, type(dict1))
# print(dict1)
# print()
#Call elements of a dictionary
#ACTUAL BEAUTY OF DICTIONARIES
# print(dict1['Neel'])
# print()
#Call all keys or values
# print(dict1.keys())
# print()
# print(dict1.values())
# print()
# print(dict1.items())
# print()
#Add item to a dictionary
dict1['neel'] = 1000
# print(dict1['neel'])
# print()
#Change values in a dictionary
dict1[string] = ints
# print(dict1)
# print()
# for oogabooga in dict1.keys():
#   print(dict1[oogabooga])
# # print()
# for item in dict1.values():
#   print(item)
# print()
#How many a's are in the string?
newDict = {}
for letter in string:
  if letter in newDict:
    newDict[letter] +=1
  else:
    newDict[letter] = 1
# print(newDict)
# print(newDict['a'])
list3 = ['the', 'apple', 'a', 'test', 'neel', 'cats', 'dont f with cats','dont f with cats','dont f with cats']
newDict2 = {}
for letter in list3:
  if letter in newDict2:
    newDict2[letter] +=1
  else:
    newDict2[letter] = 1
list4 = ['the', 'apple', 'a']
print(newDict2)
for word in list4:
  print(newDict2[word])
# for letter in string:
#   print(newDict[letter])
```
          
---

## Types of functions

There are two types of functions:

- **Built-in functions** - Functions that are built into Python.
- **User-defined functions** - Functions defined by the users themselves.

Some built-in functions:

|Function|Description|
|---|---|
|`float()`|converts to decimal number and returns it|
|`int()`|converts to integer and returns it|
|`input()`|function to take input from the user|

---

## Example

#### Grading Student Based on Marks Obtained by Making Functions

Suppose you just attended a University examination. The marks you obtained in various subjects are stored in a list like this:

```python
marks = [55, 64, 75, 80, 65]
```

**You want to find the average marks you obtained in the exam.**

**Based on the average marks you want to find your grade as:**

- **You will get Grade A if the average marks is equal to or above 80**
- **You will get Grade B if the average marks is equal to or above 60 and less than 80**
- **You will get Grade C if the average marks is equal to or above 50 and less than 60**
- **And if the average marks is less than 50, you will get Grade F**

```python
# find the average marks and return it
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    number_of_subjects = len(marks)

    average_marks = sum_of_marks/number_of_subjects

    return average_marks

# compute grade and return it
def compute_grade(average_marks):
    if average_marks >= 80.0:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'

    return grade

marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
grade =compute_grade(average_marks)

print("Your average marks is", average_marks)
print("Your grade is", grade)
```

**Output**
```
Your average marks is 67.8
Your grade is B
```

---

## Programming Task

**Can you create a program to add and multiply two numbers?**

**For this, create two functions `add_numbers()` and `multiply_numbers()`.
These functions should compute the result and return them to the function call and should print from outside the function.**


```python
# function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# function to multiply two numbers
def multiply_numbers(num1, num2):
    return num1 * num2

number1 = 5
number2 = 30

sum_result = add_numbers(number1, number2)
print("Sum is", sum_result)

product_result = multiply_numbers(number1, number2)
print("Product is", product_result)
```

**Output**

```
Sum is 35
Product is 150
```
      
## Python Coding Practice

| Python Practice Websites                   | Weblinks                            |
| ------------------------------ | ---------------------------------- |
| CodingBat Python | [📺][https://codingbat.com/python]
| Python Principles | [📺][https://pythonprinciples.com/challenges/] 
| HackerRank Python Challenges | [📺][https://www.hackerrank.com/domains/python] 
| Edabit Python Challenges | [📺][https://edabit.com/challenges/python3] 
| Holy Python Exercises  | [📺][https://holypython.com/beginner-python-exercises/] 
| Codewars  | [📺][https://www.codewars.com/collections/python-practice-1]   
      
      
[Python3 Cheat Sheet](https://github.com/FullstackAcademy/2106-UNF-RM-CYB-PT-Library/blob/main/student-resources/Python3_Cheat_Sheet.pdf)      
