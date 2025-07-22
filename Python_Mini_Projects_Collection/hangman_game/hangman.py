"""
File: hangman.py
Name: Christine
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    hangman
    """
    lives = N_TURNS
    word = random_word()
    answer = ''
    for i in range(len(word)):
        answer += '-'
    print('The word looks like: ' + answer)

    while lives > 0:
        print('You have ' + str(lives) + ' wrong guesses left.')
        guess = str(input('Your guess: ')).upper()  # Get the user's guess and convert into uppercase
        while not guess.isalpha() or len(guess) != 1:  # Check if the guess is valid
            print('Illegal format.')
            guess = str(input('Your guess: ')).upper()
        if guess in word:  # If guess is correct
            print('You are correct!')
            answer = show_the_word(guess, word, answer)
            if answer == word:
                print('You win!!')
                print('The answer is : ' + answer)
                break
            print('The word looks like: ' + answer)
        else:  # If guess is incorrect
            print('There is no ' + guess + "'s in the word.")
            answer = show_the_word(guess, word, answer)
            print('The word looks like: ' + answer)
            lives -= 1

    if lives <= 0:
        print('You are completely hung :( ')
        print('The answer is: ' + word)


def show_the_word(guess, word, answer):
    """
    :param guess: the letter that the user guesses (str)
    :param word: the solution of this game (str)
    :param answer: the current state of the word, needs to be updated in this module (str)
    :return update answer: reveals the correct letter in the string
    """
    updated_answer = ''
    for i in range(len(word)):
        if word[i] == guess:  # If the guess matches the letter in the word
            updated_answer += guess
        else:
            updated_answer += answer[i]  # Keep the previous letter in place if not correct
    return updated_answer


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
