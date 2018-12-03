# Easy challenges
def challenge1(firstname, lastname):
    return lastname + " " + firstname


print(challenge1('John', 'Doe'))


def challenge2(number):
    if number % 2 == 0:
        return "number is even"
    else:
        return "number is odd"


print(challenge2(2))


def challenge3(tbase, theight):
    return (tbase * theight) / 2


print(challenge3(5, 7))


def challenge4(number):
    if number == 0:
        return "Number is zero"
    elif number >= 1:
        return "Number is positive"
    elif number < 1:
        return "Number is negative"


print(challenge4(9))
print(challenge4(-4))
print(challenge4(0))


def challenge5():
    