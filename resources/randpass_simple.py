# this will demonstrate the use of STRINGS in a fun way
# this script is a password generator tool that will create random passwords
# there are NO functions!  it just strings and a loop
# i start with an import command to use the random module
import random

# these are all the characters i can use in my password
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# this is to get INPUT from the user for number of passwords and cast to integer
number = input('number of passwords = ? ')
number = int(number)

# this is to get INPUT from the user for the length of the password and cast to integer
length = input('password length is = ?')
length = int(length)

# now the FOR loop (iterable) to build out the [password one character at a times
# in fact, i actually use two FOR loops - one inside the other
# the first loop picks the character to use and the second loop starts to assemble the password
for p in range(number):
    password = ''
    # this second loop (nested) builds the password one character at a time
    for c in range(length):
        # this is where the IMPORT module is used -- the choice method is built into the module
        password += random.choice(chars)
    # and now show me the passwords on the screen!!!!
    print(password)
