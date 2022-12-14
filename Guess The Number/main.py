from random import randint
from art import logo

def play():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    number_of_attempts = set_difficulty(level)

    while number_of_attempts > 0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        user_guess = guess()
        check_guess(user_guess, answer)
        number_of_attempts -= 1
        if user_guess == answer:
            return
        elif number_of_attempts == 0:
            print("You've run out of guesses, you lose.")

def guess():
    return int(input("Make a guess: "))

def set_difficulty(level):
    if level == "easy":
        return 10
    else:
        return 5

def check_guess(user_guess, random_number):
    if user_guess > random_number:
        print("Too high.")
        print("Guess again.")
    elif user_guess < random_number:
        print("Too low.")
        print("Guess again.")
    else:
        print(f"You got it! The answer was {user_guess}.")

play()