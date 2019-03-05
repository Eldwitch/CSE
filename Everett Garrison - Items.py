class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)
        self.weapon_damage = 5

    def equip(self):
        print("You equip the weapon.")

    def unequip(self):
        print("You unequip your weapon.")

    def attack(self):
        print("You attack with the weapon.")


class Armor(Item):
    def __init__(self, name):
        super(Armor, self).__init__(name)
        self.armor_defense = 5

    def equip(self):
        print("You put on the armor.")

    def unequip(self):
        print("You unequip your armor.")

class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)
        self.type = 1  # Make multiple item types like keys, potions, etc.

    def consume(self):
        print("You consume the item.")


class Makeshiftsword(Weapon):
    def __init__(self):
        super(Makeshiftsword, self).__init__("Makeshift sword")

    def equip(self):
        print("You equip the Makeshift Sword.")


class Gianthand(Weapon):
    def __init__(self):
        super(Gianthand, self).__init__("Giant's hand")

    def equip(self):
        print("You equip the Giant's hand.")


class Makeshiftarmor(Armor)
    def __init__(self):
        super(Makeshiftarmor, self).__init__("Makeshift armor")

    def equip(self):
        print("You equip the Makeshift armor.")


class Giantskin(Armor):
    def __init__(self):
        super(Giantskin, self).__init__("Giant's skin")

    def equip(self):
        print("You equip the Giant's skin.")


class Healthpotion(Consumable):
    def __init__(self):
        super(Healthpotion, self).__init__("Health potion")

    def consume(self):
        print("You drink the Health potion and restore ___ health.")


class Cavekey(Consumable):
    def __init__(self):
        super(Cavekey, self).__init__("Ominous Cave Key")

    def consume(self):
        print("You think really hard about using the key and it flies out of your hand and into the lock on the "
              "cave's lock, turning the key and opening the cave for you.")
