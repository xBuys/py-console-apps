import random

method = 'rock', 'paper', 'scissors'
answer = input("Rock, paper, scissors: ")
botans = random.choice(method)

if answer == 'rock':
    if botans == 'scissors':
        print("you win")
    if botans == 'paper':
        print("you lose")
    if botans == 'rock':
        print("tied")
if answer == 'paper':
    if botans == 'rock':
        print("you win")
    if botans == 'scissors':
        print("you lose")
    if botans == 'paper':
        print("tied")
if answer == 'scissors':
    if botans == 'paper':
        print("you win")
    if botans == 'rock':
        print("you lose")
    if botans == 'scissors':
        print("tied")
