import os
from random import choice
from game_data import data
from art import logo, vs

def random_celeb():
    """returns a random celebrity from the data list"""
    return choice(data)

def format_data(celeb):
    """Convert celebrity dictionary into printable format"""
    celeb_name = celeb["name"]
    celeb_descrp = celeb["description"]
    celeb_origin = celeb["country"]
    return f"{celeb_name}, a {celeb_descrp}, from {celeb_origin}"

def comparison(guess, choice1, choice2):
    """returns boolean value based on user's guess"""
    if choice1 > choice2:
        return guess == "a"
    else:
        return guess == "b"

def start():
    print(logo)
    choiceB = random_celeb()
    score = 0
    is_correct = True

    while is_correct:
        choiceA = choiceB
        choiceB = random_celeb()

        while choiceA == choiceB:
            choiceB = random_celeb()

        print(f"Compare A : {format_data(choiceA)}.")
        print(vs)
        print(f"Against B : {format_data(choiceB)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        is_correct = comparison(guess, choiceA["follower_count"], choiceB["follower_count"])

        os.system('cls')
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")

start()