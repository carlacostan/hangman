import random
import milestone_2

def check_guess(guess): #Checks if guessed letter is in the generated word
    guess = guess.lowercase()
    if guess in milestone_2.word_list:
            print(f"Good guess! {guess} is in the word.")
    else:
            print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(): #Checks if user input is valid, and if so checks whether the guess is in the word
    
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
             check_guess(guess)
             break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
