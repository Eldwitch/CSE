class Room(object):
    def __init__(self, name, description, north=None, east=None, south=None, west=None, up=None, down=None, enter=None,
                 items=None):
        if items is None:
            items = []
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.enter = enter
        self.characters = []
        self.items = items


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.weapon_damage = damage

    def attack(self):
        print("You attack with the weapon.")


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)
        self.type = 1  # Make multiple item types like keys, potions, etc. 1 = consumables, 2 = keys


class Gold(Item):
    def __init__(self):
        super(Gold, self).__init__("Gold")
        self.gold_amount = 0


class Makeshiftsword(Weapon):
    def __init__(self):
        super(Makeshiftsword, self).__init__("Makeshift sword", 5)

    def equip(self):
        YouVars.weapon.append(self)
        print("You equip the Makeshift Sword.")


class Gianthand(Weapon):
    def __init__(self):
        super(Gianthand, self).__init__("Giant's hand", 10)

    def equip(self):
        YouVars.weapon.append(self)
        print("You equip the Giant's hand.")


class Makeshiftarmor(Armor):
    def __init__(self):
        super(Makeshiftarmor, self).__init__("Makeshift armor", 5)

    def equip(self):
        YouVars.armor.append(self)
        print("You put on the Makeshift armor.")


class Giantskin(Armor):
    def __init__(self):
        super(Giantskin, self).__init__("Giant's skin", 10)

    def equip(self):
        YouVars.armor.append(self)
        print("You put on the Giant's skin.")


class Giantsheart(Consumable):
    def __init__(self):
        super(Giantsheart, self).__init__("Giant's heart")
        self.healthadded = 50

    def consume(self):
        YouVars.max_health += self.healthadded
        print("You savagely bite into the heart, devouring it with the ferocity of the beat it once belonged to.")
        # Increase health by some amount


class Healthpotion(Consumable):
    def __init__(self):
        super(Healthpotion, self).__init__("Health potion")
        self.health_healed = 25

    def consume(self):
        YouVars.health += self.health_healed
        print("You drink the Health potion and restore 25 health.")


class Cavekey(Consumable):
    def __init__(self):
        super(Cavekey, self).__init__("Ominous Cave Key")

    def consume(self):
        F14.description = "You look around and feel an odd sense of calm here, as if you're safe for now. A signpost " \
                          "in the middle of \nthe road points in the four cardinal directions, with labels for each. " \
                          "\n'North: Another crossroads, \nEast: Strange Faerie Man Wannabe's Home and shop, and" \
                          " Piggy Fountain, \nSouth: Forest clearing,\nWest: Unlocked Cultist cave."
        F14.west = 'CSTART'
        print("You think really hard about using the key and it flies out of your hand and into the lock on the "
              "cave's entrance. The key turns itself and opens the cave for you.")


class Ironsword(Weapon):
    def __init__(self):
        super(Ironsword, self).__init__("Iron sword", 15)

    def equip(self):
        YouVars.weapon.append(self)
        print("You equip the Iron sword.")


class Ironarmor(Armor):
    def __init__(self):
        super(Ironarmor, self).__init__("Iron armor", 15)

    def equip(self):
        YouVars.armor.append(self)
        print("You put on the Iron armor.")


class Cultistbrew(Consumable):
    def __init__(self):
        super(Cultistbrew, self).__init__("Cultist's special brew. WARNING: will lower your max health and increase "
                                          "your strength.")
        self.healthremoved = 50
        self.strengthadded = 15

    def consume(self):
        YouVars.max_health = self.healthremoved
        YouVars.strength = self.strengthadded
        print("You pop the cork off of the bottle and chug the whole thing down in one go. You suddenly feel stronger,"
              " but your skin starts to feel frail, \nalmost like glass.")


class Demonhorn(Weapon):
    def __init__(self):
        super(Demonhorn, self).__init__("Demon's horn", 20)

    def equip(self):
        YouVars.weapon.append(self)
        print("You equip the Demon's horn.")

    def attack(self):
        print("You stab forward with the pointy end of the Demon's horn.")


class Demonskin(Armor):
    def __init__(self):
        super(Demonskin, self).__init__("Demon's skin", 20)

    def equip(self):
        YouVars.armor.append(self)
        print("You put on the Demon's skin.")


class Demonheart(Consumable):
    def __init__(self):
        super(Demonheart, self).__init__("Demon's heart")
        self.healthincrease = 50

    def consume(self):
        YouVars.max_health += self.healthincrease
        print("You savagely rip and tear into the heart, devouring it with the ferocity of the beast it once belonged "
              "to.")  # Increases health by some amount


class Dynamite(Consumable):
    def __init__(self):
        super(Dynamite, self).__init__("Situational Dynamite")

    def consume(self):
        C8.up = 'win_room'
        print("You light the fuse on the dynamite and it flies out of your hand and slams into the roof at the top of "
              "\nthe Ominous Cave, causing it to explode and expose a rope that leads skywards.")


class Shovel(Consumable):
    def __init__(self):
        super(Shovel, self).__init__("Shovel")

    def consume(self):
        C9.down = 'PSTART'
        print("The shovel flies off towards the small gravel area behind the rogue cultist's shop. It digs it's head"
              " into the ground and starts digging. \nAfter a small amount of digging the gravel all falls away and a "
              "large pit is revealed underneath it.")


class Character(object):
    def __init__(self, name, health, weapon, armor, strength, defense):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.strength = strength
        self.defense = defense

    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No damage is inflicted.")
        else:
            self.health -= damage - self.armor.armor_amt
            print("%s takes %d damage" % (self.name, damage - self.armor.armor_amt))
            if self.health < 0:
                self.health = 0
                print("%s has freaking died. F." % self.name)
        print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attack %s." % (self.name, target.name))
        target.take_damage(self.weapon.weapon_damage)


class YouVars:
    max_health = 100
    health = 100
    min_defense = 1
    min_strength = 1
    defense = 1
    strength = 1
    weapon = None
    armor = None


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = [Makeshiftsword(), Makeshiftarmor(), Cavekey(), Weapon("Sword", 10)]
        self.exp = 0
        self.weapon = None
        self.armor = None

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and find the variable of the room.

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]

    def equip(self, _item):
        if isinstance(_item, Weapon):
            self.weapon = _item
            print("You equip the %s weapon" % _item.name)
        elif isinstance(_item, Armor):
            self.armor = _item
            print("You equip the %s armor" % _item.name)

    def unequip(self, _item):
        if isinstance(_item, Weapon):
            self.weapon = None
            print("You put away your weapon.")
        elif isinstance(_item, Armor):
            self.armor = None
            print("You take off your armor.")

    def use(self, _item):
        print("Test")
        if type(_item) is Consumable:
            print("Test2")
            _item.consume()
            self.inventory.remove(_item)

    def take(self, _item):
        if _item not in self.inventory:
            print("U wot m8.")
        else:
            print("You take the item from off the floor.")
            self.inventory.append(_item)

    def find_item(self, item_name):
        for _item in self.inventory:
            if _item.name == item_name:
                return _item
        return None


# Items
fists = Weapon("Fists", 1)
nude = Armor("Nothing", 1)
# Test items
sword = Weapon("Sword", 10)
canoe = Weapon("Canoe", 84)
wiebe_armor = Armor("Armor of the gods", 1000000000000000000000000000)

# Characters
orc = Character("Orc", 100, sword, Armor("Generic Armor", 2), 5, 5)
wiebe = Character("Wiebe", 10000000000, canoe, wiebe_armor, 100000, 100000)

# Player character
player_c = Character("You", YouVars.health, YouVars.weapon, YouVars.armor, YouVars.strength, YouVars.defense)

# Test actions
orc.attack(wiebe)
wiebe.attack(orc)


# Room instantiation
FSTART = Room("Forest Start", "The beginning of your journey, where it all begins. There's trees around you as far as"
                              "\nthe eye can see, and right above you the trees open up to allow a ray of sunshine to"
                              "\nshine onto a pentagram that you are standing on.", 'F1', 'F2', 'F3', 'F4')
F1 = Room("Forest Clearing", "There's a mutated rat you cannot fight yet here because the dev is lazy.", 'F14', 'F2',
          'FSTART', 'F4')
F2 = Room("Forest Clearing", "There's a mutated rat you cannot fight yet here because the dev is lazy.", 'F1', 'F5',
          'F3', 'FSTART')
F3 = Room("Forest Clearing", "There's a mutated rat you cannot fight yet here because the dev is lazy.", 'FSTART', 'F2',
          'F7', 'F4')
F4 = Room("Forest Clearing", "There's a mutated rat you cannot fight yet here because the dev is lazy.", 'F1', 'FSTART',
          'F3', 'F10')
F5 = Room("A calm forest clearing", "You look around and feel an odd sense of calm here, as if you're safe for now.",
          None, 'F6', None, 'F2')
F6 = Room("A dead end.", "A giant, wide tree blocks your path forward. Luckily a giant stick lies on the ground that "
                         "looks just big \nenough for you to swing like a weapon. "
                         "Unluckily, you cannot pick it up yet.", None, None, None, 'F5')
F7 = Room("Forest clearing", "There's a mutated rat you cannot fight yet here because the dev is STILL too lazy.", 'F3',
          None, 'F8')
F8 = Room("Mutated Rat Den",
          "A disgustingly polluted rat den, filled with multiple dead rats and barely alive rat babies."
          "\n In the center of the room there's a giant, bulging rat blob spewing more pollution and"
          "\ndying rat babies. You feel a strong urge to purge this beast from this world. Sadly, the"
          "\nfight system isn't implemented yet, so you are forced to move along in utter disgust.", 'F7', None, 'F9')
F9 = Room("Dead End #2: Electric Boogaloo",
          "It's yet another dead end, or your first depending on what path you've taken now. You notice" 
          "\nsome weird armor of questionable origin, which is covered in the polluted goop the rat den" 
          "\n behind you continuously spews out.", 'F8')
F10 = Room("Faerie forest clearing entrance", "There's an ominous entrance to a more mystical, wondrous part of the"
                                              "\nforest, some tiny voices beckon you inward.", None, 'F4', None, 'F11')
F11 = Room("Faerie forest clearing", "There's a Faerie you cannot fight yet here because the dev is lazy.", 'F12',
           'F10')
F12 = Room("Faerie forest clearing",
           "There's another Faerie you cannot fight yet here because the dev is still too lazy.", None, 'F13', 'F11')
F13 = Room("Faerie forest clearing",
           "There's another Faerie you cannot fight yet here because the dev is still too lazy.", None, None, 'FS',
           'F12')
FS = Room("Faerie sword clearing", "After murdering several faeries you walk into an uncharacteristicly calm clearing "
                                   "\nwith a sword that's been forced into a large rock slab in the middle of the "
                                   "\nclearing. A light beam shine brightly upon the blade, making it shine in the "
                                   "\nlight of its own glory.", 'F13')
F14 = Room("A calm forest crossroads",
           "You look around and feel an odd sense of calm here, as if you're safe for now. A signpost in the middle of "
           "\nthe road points in the four cardinal directions, with labels for each. "
           "\n'North: Another crossroads,"
           "\nEast: Strange Faerie Man Wannabe's Home and shop, and Piggy Fountain,"
           "\nSouth: Forest clearing,"
           "\nWest: Locked up Cultist cave.", 'F17', 'F15', 'F1', None)
F15 = Room("Faerie Man's Home (Outside)", "The outside of the weird Faerie wannabe man's home. It smells of cottage "
                                          "cheese and loneliness. His home also doubles as a small shop.", None, 'F16',
           None, 'F14')
F16 = Room("Piggy Fountain", "There's a nice sense of calm here as you look at a large fountain ordained with a pig"
                             " spitting a stream of water into a round basin. \nAt the bottom of the basin you can see"
                             " something small glittering in the light.", None, None, None, 'F15')
F17 = Room("Another Crossroads", "You walk into another crossroads, and a similar sign stands in the center of the area"
                                 " to inform you of what is where."
                                 "\n'North: Nothing, you can't even go here, why are you reading this?"
                                 "\nEast: The Wooden Tower (WARNING: GIANTS LIVE HERE)"
                                 "\nSouth: The Other Crossroads"
                                 "\nWest: Another dead end'.", None, 'TSTART', 'F14', 'F18')
F18 = Room("Dead End, Again", "Another dead end with some pieces of scrap metal strewn about on the ground "
                              "haphazardly.", None, 'F17')
TSTART = Room("The First Floor of a Very Tall Tower", "A Baby Giant slumbers on the floor. You are unable to wake it up"
                                                      "\nor fight it yet because those systems are not in place yet.",
              None, None, None, None, 'T1', 'TB')
TB = Room("The Tower Basement", "You can barely see in front of yourself because of how dark it is in here.", None,
          None, None, None, 'TSTART')
T1 = Room("The second floor of the Very Tall Tower", "A Child Giant slumbers here.", None, None, None, None, 'T2', 'T1')
T2 = Room("The third floor of the Very Tall Tower", "A Teenage Giant slumbers here.", None, None, None, None, 'T3',
          'T2')
T3 = Room("The fourth floor of the Very Tall Tower", "An Adult Giant slumbers here.", None, None, None, None, 'T4',
          'T3')
T4 = Room("The second floor of the Very Tall Tower", "The Last Giant slumbers here, waking and killing it would make "
                                                     "the entire race extinct forever.",
          None, None, None, None, None, 'T3')
CSTART = Room("Ominous cave entrance", "The entrance to a damp, smelly cave. You hear chants in the distance and see "
                                       "what appears to be a small shop ahead of you, past a very tall ladder \nthat "
                                       "reaches far into the cave's y axis.", None, 'F14', None, 'F1')
C1 = Room("The bottom of a large ladder.", "You stare up the large ladder and hear the chanting faintly, the rungs "
                                           "beckoning you to grasp and climb them.", None, 'CSTART', None, 'CSHOP',
          'C2')
CSHOP = Room("A rogue cultist's shop.", "A small, humble shop set up by a former cultist. You can't buy anything yet, "
                                        "but he sure does exist.", None, 'C1', None, 'C9')

player = Player(FSTART)

directions = ['north', 'east', 'south', 'west', 'up', 'down', 'enter']
playing = True

# Controller
while playing:
    print(player.current_location.name)
    print("-" * 20)
    print(player.current_location.description)
    print("-" * 20)

    command = input(">_")
    if command.lower() in ('q', 'quit', 'exit'):
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("You're unable to go this way.")
            print("-" * 20)
    elif 'equip' in command.lower():
        item_to_equip = command[6:]

        # See if we have the item in the inventory
        try:
            item = player.find_item(item_to_equip)
            if item is None:
                raise AttributeError
            player.equip(item)
        except AttributeError:
            print("You don't have one.")
    elif 'use' in command.lower():
        item_to_use = command[4:]

        if player.find_item(item_to_use):
            player.use(item_to_use)
        else:
            print("You don't have this item.")
    elif 'take off' in command.lower():
        item_to_unequip = command[8:]

        try:
            item = player.find_item(item_to_unequip)
            if item is None:
                raise AttributeError
            player.unequip(item)
        except AttributeError:
            print("You don't have one equipped.")
    else:
        print("Command not recognized.")
