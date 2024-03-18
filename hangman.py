import random
from ascii_art import hangman_logo, hangman_pics
print(hangman_logo)

# generate a random word
word_list = [
    'insight', 'miracle', 'culture', 'ticket', 'enhancement', 'massive',
    'gravity', 'forest', 'hammer', 'lawyer', 'prison', 'matchstick',
    'snake', 'rain', 'mountain', 'minister', 'properties', 'ceremony',
    'boat', 'neighbor', 'information', 'material', 'soft', 'dependence'
             ]

random_word = random.choice(word_list)
random_word_len = len(random_word)
print(f"The word is: {random_word}, and its length is {random_word_len}")

guessed_letters_list = []
guessed_letters_string = ""

for _ in range(random_word_len):
    guessed_letters_list.append("_")

user_lives = 6
stages = hangman_pics
end_of_game = False

while not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    for position in range(random_word_len):
        if user_guess == random_word[position]:
            guessed_letters_list[position] = user_guess
    guessed_letters_string = ' '.join(guessed_letters_list)
    print(guessed_letters_string)

    if user_guess not in random_word:
        print(f"You guessed {user_guess}, that's not in the word. You lost a life!")
        user_lives -= 1
        if user_lives == 0:
            end_of_game = True
            print("You lost!")

    if "_" not in guessed_letters_list:
        end_of_game = True
        print("You won!")

    print(stages[user_lives])


