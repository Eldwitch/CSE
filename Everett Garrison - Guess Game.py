import random
random = (random.randint(1, 10))

for i in range(5):
    guess = int(input("Guess a number, any number: "))
    if guess < random:
        print("Guess is too low.")
    elif guess > random:
        print("Guess is too high.")
    elif guess == random:
        print()
        print("You win!")
        break
