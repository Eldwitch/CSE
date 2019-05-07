import csv

with open("Sales Records.csv", 'r') as bigfile:
    reader = csv.reader(bigfile)
    for row in reader:
        item_type = row[2]
        total_profit = row[13]
        print("%s made %s$." % (item_type, total_profit))
