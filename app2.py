import random

number = '123456789'
input = input("choose a number 1-9 for the bot to guess: ")
random = random.choice(number)

if random == input:
	print("bot guessed your number, " + input)
if random != input:
	print("bot guessed " + random)
	print("you guessed " + input)
