import csv

fruits_profit = 0
clothes_profit = 0
meat_profit = 0
beverages_profit = 0
office_supplies_profit = 0
cosmetics_profit = 0
snacks_profit = 0
personal_care_profit = 0
household_profit = 0
vegetables_profit = 0
baby_food_profit = 0
cereal_profit = 0

sub_africa_profit = 0
middle_east_profit = 0
australia_profit = 0
europe_profit = 0
asia_profit = 0
central_america_profit = 0
north_america_profit = 0

with open("Sales Records.csv", 'r') as bigfile:
    reader = csv.reader(bigfile)
    for row in reader:
        region = row[0]
        item_type = row[2]
        total_profit = row[13]
        if item_type == 'Fruits':
            fruits_profit += float(total_profit)
        if item_type == 'Clothes':
            clothes_profit += float(total_profit)
        if item_type == 'Meat':
            meat_profit += float(total_profit)
        if item_type == 'Beverages':
            beverages_profit += float(total_profit)
        if item_type == 'Office Supplies':
            office_supplies_profit += float(total_profit)
        if item_type == 'Cosmetics':
            cosmetics_profit += float(total_profit)
        if item_type == 'Snacks':
            snacks_profit += float(total_profit)
        if item_type == 'Personal Care':
            personal_care_profit += float(total_profit)
        if item_type == 'Household':
            household_profit += float(total_profit)
        if item_type == 'Vegetables':
            vegetables_profit += float(total_profit)
        if item_type == 'Baby Food':
            baby_food_profit += float(total_profit)
        if item_type == 'Cereal':
            cereal_profit += float(total_profit)
    profit_list = [fruits_profit, clothes_profit, meat_profit, beverages_profit, office_supplies_profit,
                   cosmetics_profit, snacks_profit, personal_care_profit, household_profit, vegetables_profit,
                   baby_food_profit, cereal_profit]
    print("Fruits made $%s." % fruits_profit)
    print("Clothes made $%s." % clothes_profit)
    print("Meat made $%s." % meat_profit)
    print("Beverages made $%s." % beverages_profit)
    print("Office Supplies made $%s." % office_supplies_profit)
    print("Cosmetics made $%s." % cosmetics_profit)
    print("Snacks made $%s." % snacks_profit)
    print("Personal Care made $%s." % personal_care_profit)
    print("Household made $%s." % household_profit)
    print("Vegetables made $%s." % vegetables_profit)
    print("Baby Food made $%s." % baby_food_profit)
    print("Cereal made $%s." % cereal_profit)
    print()
    print("The largest profit made was", max(profit_list), "dollars, made by selling Cosmetics.")
