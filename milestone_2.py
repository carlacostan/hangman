import random

word_list = ["watermelon", "raspberry", "kiwi", "fig", "lemon"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please choose a single letter: ")
print("You chose:", guess)

if len(guess) == 1 and guess.isalpha():
    print("Nice")
else:
    print("Oops! That is not a valid input.")