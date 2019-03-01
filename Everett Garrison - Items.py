class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)
        self.weapon_damage = 5

    def equip(self):
        print("You wield the weapon.")

    def attack(self):
        print("You attack with the weapon.")


class Armor(Item):
    def __init__(self, name):
        super(Armor, self).__init__(name)
        self.armor_defense = 5

    def equip(self):
        print("You put on the armor.")


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)
        self.type = 1  # Make 3 potion types, one heals, one modifies something, and the last one does something else.

    def consume(self):
        print("You consume the item.")
