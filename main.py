from random import choice
import os

print("Country Guessing Game")
print("Welcome to the Guessing game. Your objective is to guess the country You have only 5 guesses each!")


def initialize_list():
    global words
    with open('countries.txt', 'r') as file:
        c = file.readlines()
        words = []
        for i in c:
            e = i.strip().lower()
            words.append(e)


initialize_list()
secret_word = choice(words).lower()
guess = None
guess_count = 0
guess_limit = 10
out_of_guesses = False

while True:

    if guess != secret_word and not (out_of_guesses):
        guess = input("Enter guess: ").lower()
        # print("The answer is", secret_word)
        guess_count += 1
        if guess_count == 3:
            firstletter = secret_word[0]
            print("It starts with the letter", firstletter)
        elif guess_count == 5:
            secondletter = secret_word[1]
            print("The second letter is", secondletter)
            continue
        elif guess_count == 7:
            thirdletter = secret_word[2]
            print("The third letter is", thirdletter )

        elif guess_count == 8:
            fourthletter = secret_word[3]
            print("Last clue, the fourth letter is", fourthletter )

        elif guess_count == 9:
            print("You only have one more guess!")
        
        
        elif guess_count == 10:
            out_of_guesses = True
            print("Your out of guesses :(")
            print("The correct answer is", secret_word.capitalize())
            exit()
    else:
        print("You got the correct answer, You win!")
        exit()
