# Creating a list
fruit = ['apples', 'oranges', 'blackberries', 'strawberries',
         'blueberries', 'raspberries', 'pineapple', 'mango', 'coconut']  # USE SQUARE BRACKETS!
print(fruit)

# Pulling items from a list
print(fruit[1])

# Getting the length of a list
print(len(fruit))
print("The length of the list is %d" % len(fruit))

# Modifying Lists
fruit[8] = 'Banana'
print(fruit)

# Looping through Lists
for item in fruit:
    print(item)

'''
1. Make a list
2. change the 3rd thing in the list
3. print the item
4. print the full list
'''
print()

fears = ['Life', 'Disappointment', 'Jeff', 'Myself', 'The monster in my closet']

fears[2] = 'Humphrey'
print(fears[2])
print()

for item2 in fears:
    print(item2)

food_list = ["chicken", "chick", "gobbler", "boneless chicken", "bone-full chicken", "chicken nuggers",
             "chicken tendies", "chicken strippers", ]
