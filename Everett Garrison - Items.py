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
        print("You take off your armor.")


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)
        self.type = 1  # Make multiple item types like keys, potions, etc.

    def consume(self):
        print("You consume the item.")


class Gold(Item):
    def __init__(self):
        super(Gold, self).__init__("Gold")
        self.gold_amount = 0


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


class Makeshiftarmor(Armor):
    def __init__(self):
        super(Makeshiftarmor, self).__init__("Makeshift armor")

    def equip(self):
        print("You put on the Makeshift armor.")


class Giantskin(Armor):
    def __init__(self):
        super(Giantskin, self).__init__("Giant's skin")

    def equip(self):
        print("You put on the Giant's skin.")


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
              "cave's entrance. The key turns itself and opens the cave for you.")


class Ironsword(Weapon):
    def __init__(self):
        super(Ironsword, self).__init__("Iron sword")

    def equip(self):
        print("You equip the Iron sword.")


class Ironarmor(Armor):
    def __init__(self):
        super(Ironarmor, self).__init__("Iron armor")

    def equip(self):
        print("You put on the Iron armor.")


class Cultistbrew(Consumable):
    def __init__(self):
        super(Cultistbrew, self).__init__("Cultist's special brew")

    def consume(self):
        print("You pop the cork off of the bottle and chug the whole thing down in one go. You suddenly feel stronger,"
              " but your skin starts to feel frail, \nalmost like glass.")


class Demonhorn(Weapon):
    def __init__(self):
        super(Demonhorn, self).__init__("Demon's horn")

    def equip(self):
        print("You equip the Demon's horn.")

    def attack(self):
        print("You stab forward with the pointy end of the Demon's horn.")


class Demonskin(Armor):
    def __init__(self):
        super(Demonskin, self).__init__("Demon's skin")

    def equip(self):
        print("You put on the Demon's skin.")


class Dynamite(Consumable):
    def __init__(self):
        super(Dynamite, self).__init__("Situational Dynamite™")

    def consume(self):
        print("You light the fuse on the dynamite and it flies out of your hand and slams into the roof at the top of "
              "\nthe Ominous Cave, causing it to explode and expose a rope that leads skywards.")
