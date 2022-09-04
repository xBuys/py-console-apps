import random

numbers = '12345789'
input = input("choose a number between 1-9: ")
random = random.choice(numbers)
if input == random:
	print("win")
if input != random:
	print("bot chose " + random)
	print("lose")