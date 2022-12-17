import os
import random
from art import logo

def deal_card(cards):
    return random.choice(cards)

def calculate_score(player_cards):
    score = sum(player_cards)
    if score > 21 and 11 in player_cards:
        ace_index = player_cards.index(11)
        player_cards[ace_index] = 1
        score -= 10
    if score == 21 and len(player_cards) == 2:
        return 0
    return score

def results(user_score, opponent_score):
    if opponent_score == user_score:
        print("Draw 🙃")
    elif user_score == 0:
        print("BlackJack! You win. 😃")
    elif opponent_score == 0:
        print("Opponent BlackJack! You lose. 😭")
    elif user_score > 21:
        print("You went over. You lose 😭")
    elif opponent_score > 21:
        print("Opponent went over. You win 😃")
    elif user_score > opponent_score:
        print("You win 😃")
    else:
        print("You lose 😭")

def play():
    os.system('cls')
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = random.sample(cards, 2)

    opponent_cards = random.sample(cards, 2)
    opponent_score = calculate_score(opponent_cards)

    should_continue = True

    while should_continue:
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {opponent_cards[0]}")
        if (user_score == 0) or (opponent_score == 0) or (user_score > 21):
            should_continue = False
        else:
            next_move = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if next_move == "y":
                user_cards.append(deal_card(cards))
            else:
                should_continue = False
    while opponent_score < 17 and opponent_score != 0:
        opponent_cards.append(deal_card(cards))
        opponent_score = calculate_score(opponent_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {opponent_cards}, final score: {opponent_score}")

    results(user_score = user_score, opponent_score = opponent_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play()