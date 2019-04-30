import csv


def validate(num: str):
    if is_it_even(num) and is_it_odd(num):
        return True
    return False


def is_it_even(num: str):
    second_num = int(num[1])  # This is the second number
    if second_num % 2 == 0:
        return True
    return False


def is_it_odd(num: str):
    first_num = int(num[0])  # This is the first number
    if first_num % 2 != 0:
        return True
    return False


# with open("Book1.csv", 'r') as old_csv:
#     reader = csv.reader(old_csv)
#     for row in reader:
#         old_number = row[0]
#         print(old_number)
#         new_number = int(old_number)
#         new_number += 1
#         print(new_number)
#
# # OR
#
#     for row in reader:
#         old_number = row[0]
#         print(int(old_number) + 1)
#         print(old_number)

# with open("Book1.csv", 'r') as old_csv:
#     with open('MyNewFile.csv', 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#
#         for row in reader:
#             #  old_number = int(row[0]) + 1
#             old_num = row[0]  # This is a string
#             first_num = int(old_num[0])  # This is the first number
#             if first_num == 4:
#                 writer.writerow(row)
#     print("Done!")

def reverse_it(string):
    return string[::-1]


print(reverse_it("!dlroW olleH"))


with open("Book1.csv", 'r') as old_csv:
    with open('MyNewFile.csv', 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            #  old_number = int(row[0]) + 1
            old_num = row[0]  # This is a string
            first_num = int(old_num[0])  # This is the first number
            if validate(old_num):
                writer.writerow(row)
    print("Done!")
