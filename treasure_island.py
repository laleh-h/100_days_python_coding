from ascii_art import treasure_island_logo
from emoji_unicodes import screaming, partying

print(treasure_island_logo)

choice_1 = input("Your at a junction, would you like to turn 'Left' or 'Right'? ").lower()

if choice_1 == 'left':
    choice_2 = input("You\'ve come to a lake. There is an island in the middle of the lake.\
    Type 'wait' to wait for a boat or 'swim' to swim across. ").lower()

    if choice_2 == 'wait':
        choice_3 = input("You arrived at the island unharmed. There is a house with 3 doors.\
        One red, one yellow and one blue. Which colour do you choose?").lower()

        if choice_3 == 'yellow':
            print(f"You found the treasure! You won! {partying}")
        elif choice_3 == 'blue':
            print(f"You enter a room of beasts. Game Over! {screaming}")
        else:
            print(f"You\'re attacked by an angry trout. Game Over! {screaming}")
    else:
        print(f"You chose a door that doesn't exist. Game Over! {screaming}")
else:
    print(f"Game Over! You fell into a hole! {screaming}")
