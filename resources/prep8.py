# this is a better guessing game that keeps you guessing until you are correct
# it uses the IMPORT command and also the INPUT command
# the INPUT is convertetd into an integer... so that means if you type a string or boolean or float... it breaks! (try it)
# so the WHILE loop condition depends on the guess not being correct (!=)
import random
correct = random.randint(1, 10)
guess = input("Enter your guess: ")
guess = int(guess)
while guess != correct:
	if guess > correct:
		print("You've guessed too high. Try guessing lower.")
	else:
		print("You've guessed too low. Try guessing higher.")
	guess = int(input("Enter your guess: "))
print("Congratulations! You've guessed correctly.")
