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
print()

food_list = ["pizza", "tamales", "tacos", "pie", "enchiladas", "burrito",
             "sushi", "poke", "flan", "poutine", "noodles", "chicken",
             'chili', "Hot wings", "salmon", "chips", "lasagna", "soup",
             "fettuccine", "salad", "carne asada"]

# Slicing
print(food_list[2:5])
print(food_list[3:4])
print(food_list[10:])
print(food_list[:5])

# Adding stuff to a list (part 1)
food_list.append("oranges")
food_list.append("bacon")
print(food_list)
# Everything is in the form Object.method(parameters)

# Adding to a list (not at the end)
food_list.insert(2, "Goat")
print(food_list)

# Removing from a list
food_list.remove("tacos")
food_list.remove("pie")
print(food_list)
# This removes the specific item from the list

# Removing from a list (pt 2)
# Sometimes, you don't know what is in the list, but you know
# you want to get rid of something at a specific index
food_list.pop(0)
print(food_list)
# Notice that "pizza" is no longer in the list because was is at index 0.

# Practice time...
"""
1. Make a new list with 3 items
2. Add a 4th item to the list
3. Remove one of the first three items from the list.
I'll come around and check progress/fix errors.
"""

# Finding things in a list
print(food_list.index("chicken"))
# This printed 9 for me, so chicken must be at index 9.
# This is an easy way of finding things in a list.

# Things I notice people do:
# Some people have made lists with parentheses instead of brackets
brands = ("apple", "samsung", "HTC")
# This is a TUPLE, not a list. Tuples are immutable (cannot be changed)

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

# Hangman hints
for i in range(len(list1)):  # i goes through all indices
    if list1[i] == "u":  # if we find a "U"
        list1.pop(i)  # Remove the i-th index
        list1.insert(i, "*")  # Put a * there instead

# Changing back into a string (list→string)
print("".join(list1))
