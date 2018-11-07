import random
money = 15
Round = 0
most_money = 15
most_money_round = 0

while money > 0:
    d6 = random.randint(1, 6)
    d62 = random.randint(1, 6)
    money -= 1
    Round += 1
    if d6 + d62 == 7:
        money += 5
    if money > most_money:
        most_money = money
        most_money_round = Round

print("Highest round:", Round)
print("Most money:", most_money)
print("Round you had the most money:", most_money_round)