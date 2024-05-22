import random

#List of fruits
word_list = ["watermelon", "raspberry", "kiwi", "fig", "lemon"]
print(word_list)

#Generating a random word from word_list
word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter: ")