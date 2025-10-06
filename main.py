import random

print("Welcome to Number Guessing Game!")
number = random.randint(1, 20)  # computer chooses number 1-20
guess = None
attempts = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
