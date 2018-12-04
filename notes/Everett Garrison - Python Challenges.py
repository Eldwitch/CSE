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


def challenge5(radius):
    return 3.14159265359 * radius ** 2


print(challenge5(1.1))


def challenge6(radius):
    return 4/3 * 3.14159265359 * radius ** 3


print(challenge6(1.1))


def challenge7(n):
    return n+n*n+n*n*n


print(challenge7(5))


def challenge8(number):
    if 1850 <= number < 2000:
        return "Number is within 150 of 2000"
    elif 1850 > number:
        return "Number isn't within 150 of 2000"
    elif 2150 >= number > 2000:
        return "Number is within 150 of 2000"
    elif 2150 < number:
        return "Number isn't within 150 of 2000"


print(challenge8(1900))
print(challenge8(100))
print(challenge8(2100))
print(challenge8(3000))


def challenge9(letter):
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return "Letter is a vowel"
    else:
        return "Letter is not a vowel"


print(challenge9("e"))
print(challenge9("h"))
