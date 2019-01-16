import random
import string
Words = ["singular", "bees", "SCREAMING", "satan", "god", "hello",
         "why", "seven", "zoinks", "taste", "swivel", "egg", "thirsty", "thirteen",
         "joke", "demon", "store", "what..?", "communism", "Hello World", "Everett"]

win = False
word = random.choice(Words)
word_list = list(word)
print(word)
guess = 8
alphabet = list(string.ascii_letters)
guessed_letters = []

for i in range(len(word)):
    if word[i] in alphabet:
        word_list.pop(i)
        word_list.insert(i, "*")
print("".join(word_list))

while guess > 0 and not win:
    guess1 = input("Guess: ")
    print(guess)
    guessed_letters.append(guess1.lower())
    for i in range(len(word)):
        if word[i].lower() in guessed_letters:
            word_list.pop(i)
            word_list.insert(i, word[i])
    if guess1.lower() not in word_list and guess1.upper() not in word_list:
        guess -= 1
    print("".join(word_list))
    if '*' not in word_list:
        win = True
        print("You're winner!")
