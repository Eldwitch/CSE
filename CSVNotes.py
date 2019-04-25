import csv

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

with open("Book1.csv", 'r') as old_csv:
    with open('MyNewFile.csv', 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            #  old_number = int(row[0]) + 1
            old_number = row[0]
            first_num = int(old_number[0])
            if first_num == 4:
                writer.writerow(row)
    print("Done!")
