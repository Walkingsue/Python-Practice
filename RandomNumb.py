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
    guess = input(f"Guess a number between {low} and {high}: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess > high or guess < low:
            print("Out of bounds! Try again.")
            print(f"Please select a number between {low} and {high}.")
        elif guess > numb:
            print("Too high!")
        elif guess < numb:
            print("Too low!")
        else:
            print(f"That is correct! The number was {numb}.")
            break
    else:
        print("That is not a number! Please try again.")
        print(f"Please select a number between {low} and {high}.")

print(f"You guessed it in {guesses} tries.")