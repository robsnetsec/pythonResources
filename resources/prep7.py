# this is the simplest of the number guessing games
# we use the IMPORT command to bring in some pre-written code for choosing a random number in python
# and the whole program just runs once from top to bottom... there is NO LOOPING!
# please note the use of spacing and also the guess variable converts the input into an integer on the same line... nice!!
# and please try to break the program by enterint STR or FLOAT or BOOL values or a blank
import random
hidden = random.randrange(1, 201)
print(hidden)
guess = int(input("Please enter your guess: "))
if guess == hidden:
    print("Hit!")
elif guess < hidden:
    print("Your guess is too low")
else:
    print("Your guess is too high")
