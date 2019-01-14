import random
import string
Words = ["singular", "bees", "SCREAMING", "satan", "god", "hello",
         "why", "seven", "zoink", "taste", "swivel", "egg", "thirsty", "thirteen",
         "joke", "demon", "store", "..."]

win = 0
word = random.choice(Words)
word_list = list(word)
print(word)
guess = 6
alphabet = list(string.printable)
guessed_letters = []


for i in range(len(word)):
    if word[i] in alphabet:
        word_list.pop(i)
        word_list.insert(i, "*")
print("".join(word_list))

while guess >= 0:
    guess1 = input("Guess: ")
    guess -= 1  # fix later
    guessed_letters.append(guess1)
    for i in range(len(word)):
        if word[i] in guessed_letters:
            word_list.pop(i)
            word_list.insert(i, word[i])
    print("".join(word_list))
