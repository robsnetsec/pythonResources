'''
PRO TIP == you can comment out a WHOLE LOTTA LINES by using 3 quotes at start and at end
Random Password Generator using Python
Author == Neel Amin
Date == Sat, May 28th, 2021
Use = demo for python class in cyber bootcamp
'''

# first we import the necessary modules!
# one for the random number picker and one for the methods to use with strings
import random
import string

# let's give this script a nice title to welcome the user!!
print('Howdy, and welcome to the best Password Generator!')

# input command to get the length of password -- and also cast it into an integer data type -- all within single line
length = int(input('\nEnter the length of password: '))                      

# here we define the data formats that we will use -- basically all the characters on a keyboard
# UPPER, lower, numbers and symbols == the four main elements of a complex password
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combine all the data strings above into one jumbo string with all the various combinations
all = lower + upper + num + symbols

# use the random module to pick a character from the huge string we created above
# also make it the 'length' that was provided by the user and assign it to 'temp' variable
temp = random.sample(all,length)

# now create the password - use JOIN method that nicely concatenates all together with a particular delimiter - in this case EMPTY space 
password = "".join(temp)

# lastly we print the password to the screen
print(password)
