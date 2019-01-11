import random
Words = ["singular", "bees", "SCREAMING", "satan", "god", "hello",
         "why", "seven", "zoink", "taste", "swivel", "egg", "thirsty", "thirteen",
         "joke", "demon", "store", "..."]

word = random.choice(Words)
print(word)
guess = 6
guessed_letters = []

for i in range(len(word)):
    if word[i] == word:
        word.pop(i)
        word.insert(i, "*")

guess1 = input("Guess: ")
guessed_letters.append(guess1)
print(guessed_letters)
