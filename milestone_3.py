import milestone_2

#if __name__ == "__main__":
    
    #ask_for_input()

def ask_for_input(): #Checks if user input is valid, and if so checks whether the guess is in the word
    
    while True:
        guess = input("Guess a letter: ")
        length_of_guess = len(guess) 
        guess_is_alphabetical_character = guess.isalpha()
        if length_of_guess == 1 and guess_is_alphabetical_character:
             check_guess(guess)
             print("You chose:", guess)
             break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    
def check_guess(guess): #Calls function to check if guessed letter is in the generated word

    guess = guess.lower()
    if guess in milestone_2.word:
            print(f"Good guess! {guess} is in the word.")
    else:
            print(f"Sorry, {guess} is not in the word. Try again.")

