import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_move = int(input("Enter 0 for Rock, 1 for Paper & 2 for Scissors.\n"))

if user_move < 0 or user_move > 2:
    print("You have entered an invalid number, you lose.")
else:
    print(game_images[user_move])
    
    print("Computer choose:")
    
    computer_move = random.randint(0, 2)
    
    print(game_images[computer_move])
    
    if computer_move == user_move:
        print("Draw!")
    elif (user_move == 0 and computer_move == 2) or (user_move == 1 and computer_move == 0) and (user_move == 2 and computer_move == 0):
        print("You Wins!")
    else:
        print("You loose.")