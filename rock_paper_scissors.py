
import random
from ascii_art import rock, scissors, paper

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
bot_choice = random.randint(0, 2)

choice_graphic = [rock, paper, scissors]
choice_text = ["Rock", "Paper", "Scissors"]


user_choice_text = choice_text[user_choice]
bot_choice_text = choice_text[bot_choice]
user_choice_graphic = choice_graphic[user_choice]
bot_choice_graphic = choice_graphic[bot_choice]


if user_choice == bot_choice:
    print("You both chose: {user_choice_text} \n")
    print(user_choice_graphic)
    print("It's a draw!")

elif user_choice == 0 and bot_choice == 1:  # rock loses against paper
    print(f"Your choice is: {user_choice_text}  \n")
    print(user_choice_graphic)
    print(f"Bot's choice is: {bot_choice_text}  \n")
    print(bot_choice_graphic)
    print("You lost!")
elif user_choice == 0 and bot_choice == 2:  # rock wins against scissors
    print(f"Your choice is: {user_choice_text}  \n")
    print(user_choice_graphic)
    print(f"Bot's choice is: {bot_choice_text}  \n")
    print(bot_choice_graphic)
    print("You won!")

elif user_choice == 1 and bot_choice == 0:  # paper wins against rock
    print(f"Your choice is: {user_choice_text}  \n")
    print(user_choice_graphic)
    print(f"Bot's choice is: {bot_choice_text}  \n")
    print(bot_choice_graphic)
    print("You won!")

elif user_choice == 1 and bot_choice == 2:  # paper loses against scissors
    print(f"Your choice is: {user_choice_text}  \n")
    print(user_choice_graphic)
    print(f"Bot's choice is: {bot_choice_text}  \n")
    print(bot_choice_graphic)
    print("You lost!")

elif user_choice == 2 and bot_choice == 0:  # scissors lose against rock
    print(f"Your choice is: {user_choice_text}  \n")
    print(user_choice_graphic)
    print(f"Bot's choice is: {bot_choice_text}  \n")
    print(bot_choice_graphic)
    print("You lost!")

elif user_choice == 2 and bot_choice == 1:  # scissors wins against paper
    print(f"Your choice is: {user_choice_text}  \n")
    print(user_choice_graphic)
    print(f"Bot's choice is: {bot_choice_text}  \n")
    print(bot_choice_graphic)
    print("You Won!")