import csv

test_num = "4556737586899855"
test_num2 = "8148064838470700"
end_digit = 0


def validate(num: str):
    last_num = int(num[15])
    next_num = drop_last_digit(num)
    # print(next_num)
    # print(str(next_num))
    sum = odd_numbers_stuff(''.join(next_num))
    return sum == last_num


def drop_last_digit(num: str):
    new_num = list(num[14::-1])  # The number that it processes but without the last digit
    return new_num


def odd_numbers_stuff(num: str):
    odd_numbers = []
    even_numbers = []
    for index in range(0, 15, 2):
        odd_numbers.append(int(num[index]))

    for index in range(1, 15, 2):
        even_numbers.append(int(num[index]))

    for i in range(len(odd_numbers)):
        odd_numbers[i] *= 2
        if odd_numbers[i] > 9:
            odd_numbers[i] -= 9
    all_nums = even_numbers + odd_numbers
    sum = 0
    for i in all_nums:
        sum += i

    sum %= 10
    return sum


print(validate(test_num))

print(validate(test_num2))


with open("Book1.csv", 'r') as old_csv:
    with open('MyNewFile.csv', 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            number = row[0]  # This is a string
            print(number)
            if validate(number):
                writer.writerow(row)
    print("Done!")
