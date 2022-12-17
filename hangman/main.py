import random
from art import stages, logo
from game_data import word_list

print(logo)

lives = 6

chosen_word = random.choice(word_list)

display = []

for index in range(len(chosen_word)):
    display.append("_")

while lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")
    elif guess in chosen_word:
        for index in range(len(chosen_word)):
            if guess == chosen_word[index]:
                display[index] = guess
    else:
        print(f"You guesssed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    print(' '.join(display))
    print(stages[lives])
    if "_" not in display:
        print("You win!")
        break
    elif lives == 0:
        print("You lose")