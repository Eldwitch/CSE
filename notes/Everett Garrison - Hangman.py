import random
Words = ["bepis", "singular", "bees", "screaming", "satan", "god", "hello",
         "why", "nine", "zoink", "taste", "swivel", "egg", "thirsty", "fifteen",
         "joke", "scoobis", "demon", "ech", "store"]

word = random.randint(0, 19)
random_word = Words[word]
print(random_word)
guess = 6

if guess > 0:
    if Words == "bepis":
        input("Guess a letter ")
