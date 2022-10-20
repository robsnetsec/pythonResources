# this is the best example of the number guessing game
# this uses IMPORT and INPUT and also includes a counter to keep the number of attempted guesses under 5
# so basically you get 4 chances to guess the number
# that is the condition of the WHILE loop.... are the number of guesses under 5
# and if you guess 5 times, it will just tell you the number
# also please note the use of += to increase the counter by 1 in each loop
# also there are no ELIF statements, just multiple if's and one else
# also, it asks for your name to make a bit more personalized :)
import random
number = random.randint(1, 10)
player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('okay! '+ player_name + ' I am Guessing a number between 1 and 10:')
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))
