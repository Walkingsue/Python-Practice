from random import random
import random

low = 1
high = 100

numb = random.randint(low, high)

print(numb)

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

random.shuffle(cards)

print(cards)

options = ['rock', 'paper', 'scissors']

choice = random.choice(options)

print(choice)

guesses = 0

while True:
    guess = int(input(f"Guess a number between {low} and {high}: "))
    guesses += 1
    if guess > numb:
        print("Too high!")
    elif guess < numb:
        print("Too low!")
    else:
        print(f"That is correct! The number was {numb}.")
        break

print(f"You guessed it in {guesses} tries.")