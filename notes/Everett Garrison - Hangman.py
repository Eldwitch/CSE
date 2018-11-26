import random
Words = ["bepis"]
""""singular", "bees", "screaming", "satan", "god", "hello",
         "why", "nine", "zoink", "taste", "swivel", "egg", "thirsty", "fifteen",
         "joke", "scoobis", "demon", "ech", "store"""""
Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
            "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]
word = random.randint(0, 19)
random_word = Words[word]
print(random_word)
guess = 6

if guess > 0:
    if Words == "bepis":
        input("Guess a letter ")
