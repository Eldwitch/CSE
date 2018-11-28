print("This is a mad lib, please input the type of word the program asks for as it asks you for them.")
Words = [
    input("Noun: "),
    input("Adjective: "),
    input("Occupation: "),
    input("Verb: "),
    input("Plural noun: "),  # Original plural noun, index 4
    input("Type of food: "),
    input("Verb ending in 'ed': "),
    input("Weapon: "),
    input("Article of clothing: "),
    input("Type of workout: "),
    input("Proper noun referring to a place: "),
    input("Sound: "),
    input("Human organ: ")
]

print()

print("Your name is %s." % Words[0])
print("You are a %s %s." % (Words[1], Words[2]))
print("Today you must %s the %s." % (Words[3], Words[4]))
print("The reason you are doing this is because the %s ate your %s." % (Words[4], Words[5]))
print("This was the last straw for you, they have went over the line, and for that they must be %s." % Words[6])
print("You arm yourself with a %s and put on your favorite %s." % (Words[7], Words[8]))
print("After all of this, you do some extreme %s." % Words[9])
print("After what feels like hours of walking you arrive at %s's %s" % (Words[4], Words[10]))
print("When you enter you have a glorious battle with %s that ends in your victory." % Words[4])
print("As a sign of ultimate dominance you let out a fierce %s." % Words[11])
print("After the battle, you return home and take a long nap to rest your troubled %s." % Words[12])
