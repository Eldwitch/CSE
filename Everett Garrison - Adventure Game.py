def fight(target):
    print("You get into a fight with %s" % target.name)
    while YouVars.health > 0 and target.health > 0:
        if YouVars.armor is None:
            player_c.armor = nude
        if YouVars.weapon is None:
            player_c.weapon = fists
        lcommand = input("What do you want to do? ")

        if "attack" in lcommand.lower():
            player_c.attack(target)
            target.attack(player_c)

        elif "attack" not in lcommand:
            target.attack(player_c)


class Room(object):
    def __init__(self, name, description, north=None, east=None, south=None, west=None, up=None, down=None, items=None,
                 enemies=None):
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
        self.characters = []
        self.items = items
        self.enemies = enemies


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

    def consume(self):
        print("You use the item.")


class Makeshiftsword(Weapon):
    def __init__(self):
        super(Makeshiftsword, self).__init__("Makeshift sword", 5)

    def equip(self):
        YouVars.weapon.append(self)
        print("You equip the Makeshift Sword.")


class Gianthand(Weapon):
    def __init__(self):
        super(Gianthand, self).__init__("Giant hand", 15)

    def equip(self):
        YouVars.weapon.append(self)
        print("You equip the Giant's hand.")


class Makeshiftarmor(Armor):
    def __init__(self):
        super(Makeshiftarmor, self).__init__("Makeshift armor", 5)

    def equip(self):
        YouVars.armor.append(self)
        print("You put on the Makeshift armor.")
        F9.description = "It's yet another dead end, or your first depending on what path you've taken now. " \
                         "You can exit to the North."


class Giantskin(Armor):
    def __init__(self):
        super(Giantskin, self).__init__("Giant skin", 10)

    def equip(self):
        YouVars.armor.append(self)
        print("You put on the Giant's skin.")


class Giantsheart(Consumable):
    def __init__(self):
        super(Giantsheart, self).__init__("giant heart")
        self.healthadded = 50

    def consume(self):
        YouVars.max_health += self.healthadded
        print("You savagely bite into the heart, devouring it with the ferocity of the beat it once belonged to.")
        # Increase health by some amount


class Healthpotion(Consumable):
    def __init__(self):
        super(Healthpotion, self).__init__("health potion")
        self.health_healed = 25

    def consume(self):
        YouVars.health += self.health_healed
        print("You drink the Health potion and restore 25 health.")


class Cavekey(Consumable):
    def __init__(self):
        super(Cavekey, self).__init__("cave key")
        self.level_change = 'CSTART'

    def consume(self):
        F14.description = "You look around and feel an odd sense of calm here, as if you're safe for now. A signpost " \
                          "in the middle of \nthe road points in the four cardinal directions, with labels for each. " \
                          "\n'North: Another crossroads, \nEast: Strange Faerie Man Wannabe's Home and shop, and" \
                          " Piggy Fountain, \nSouth: Forest clearing,\nWest: Unlocked Cultist cave."
        F14.west = self.level_change
        print("You think really hard about using the key and it flies out of your hand and into the lock on the "
              "cave's entrance. The key turns itself and opens the cave for you.")


class Ironsword(Weapon):
    def __init__(self):
        super(Ironsword, self).__init__("Iron sword", 10)

    def equip(self):
        YouVars.weapon.append(self)
        print("You equip the Iron sword.")
        FS.description = "A strangely calm clearing with a cracked rock slab in the middle of it. " \
                         "\nYou are able to exit to the North."


class Ironarmor(Armor):
    def __init__(self):
        super(Ironarmor, self).__init__("Iron armor", 15)

    def equip(self):
        YouVars.armor.append(self)
        print("You put on the Iron armor.")


class Cultistbrew(Consumable):
    def __init__(self):
        super(Cultistbrew, self).__init__("cultist brew")
        self.healthremoved = 25

    def consume(self):
        YouVars.max_health = self.healthremoved
        print("You pop the cork off of the bottle and chug the whole thing down in one go."
              "\nYour skin suddenly starts to feel frail, almost like glass. Your maximum health has been lowered by "
              "50!")


class Demonhorn(Weapon):
    def __init__(self):
        super(Demonhorn, self).__init__("Demon horn", 20)

    def equip(self):
        YouVars.weapon.append(self)
        print("You equip the Demon's horn.")

    def attack(self):
        print("You stab forward with the pointy end of the Demon's horn.")


class Demonskin(Armor):
    def __init__(self):
        super(Demonskin, self).__init__("Demon skin", 20)

    def equip(self):
        YouVars.armor.append(self)
        print("You put on the Demon's skin.")


class Demonheart(Consumable):
    def __init__(self):
        super(Demonheart, self).__init__("demon heart")
        self.healthincrease = 50

    def consume(self):
        YouVars.max_health += self.healthincrease
        print("You savagely rip and tear into the heart, devouring it with the ferocity of the beast it once belonged "
              "to.")  # Increases health by some amount


class Dynamite(Consumable):
    def __init__(self):
        super(Dynamite, self).__init__("situational dynamite")
        self.level_change = 'WIN_ROOM'

    def consume(self):
        C8.up = self.level_change
        print("You light the fuse on the dynamite and it flies out of your hand and slams into the roof at the top of "
              "\nthe Ominous Cave, causing it to explode and expose a rope that leads skywards.")


class Shovel(Consumable):
    def __init__(self):
        super(Shovel, self).__init__("shovel")
        self.level_change = 'PSTART'

    def consume(self):
        C9.down = self.level_change
        print("The shovel flies off towards the small gravel area behind the rogue cultist's shop. It digs it's head"
              " into the ground and starts digging. \nAfter a small amount of digging the gravel all falls away and a "
              "large pit is revealed underneath it.")


class Pigheal(Consumable):
    def __init__(self):
        super(Pigheal, self).__init__("piggy potion")

    def consume(self):
        YouVars.health = YouVars.max_health
        print("You down the bottled Piggy Fountain water. You feel any wounds or damage taken you had mend together and"
              " heal themselves. Health fully restored!")


class Disappointment(Consumable):
    def __init__(self):
        super(Disappointment, self).__init__("Scrap metal")

    def consume(self):
        print("You use the sc- Wait a minute, this isn't scrap metal, these are stickers."
              "\n The disappointment you feel as you realize that you were cheated out of a crafting system physically "
              "hurts you. You lose 1 HP.")
        YouVars.health -= 1


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

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


# Items
fists = Weapon("Fists", 2)
nude = Armor("Nothing", 1)
stick = Weapon("Big stick", 4)


class YouVars:
    max_health = 100
    health = 100
    weapon = None
    armor = None


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []
        self.level = 1
        self.exp = 0

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
            YouVars.weapon = _item
            print("You equip the %s." % _item.name)
        elif isinstance(_item, Armor):
            YouVars.armor = _item
            print("You equip the %s." % _item.name)

    def unequip(self, _item):
        if isinstance(_item, Weapon):
            YouVars.weapon = None
            print("You put away your weapon.")
        elif isinstance(_item, Armor):
            YouVars.armor = None
            print("You take off your armor.")

    def use(self, _item):
        _item.consume()
        self.inventory.remove(_item)

    def find_item(self, item_name):  # Takes the name of the item and returns the item itself
        for _item in self.inventory:
            if _item.name == item_name:
                return _item
        return None

    def pick_up(self):
        if len(player.current_location.items) > 0:
            print("You pick up the item(s).")
            for _item in player.current_location.items:
                self.inventory.append(_item)
            player.current_location.items = []

    def view_inventory(self):
        print("Your health is at %i/%i" % (YouVars.health, YouVars.max_health))
        print("-" * 20)
        print("You have %s equipped as your weapon and %s equipped as your armor." % (YouVars.weapon, YouVars.armor))
        print("-" * 20)
        for _item in player.inventory:
            print("You have a(n) %s." % _item.name)
            print("-" * 20)


# Player character
player_c = Character("You", YouVars.health, YouVars.weapon, YouVars.armor)

# Enemy
m_rat = Character("Mutated Rat", 3, Weapon("Claw", 2), Armor("Rat hide", 1))
fairy = Character("Faerie", 5, Weapon("Nails", 3), Armor("Faerie cloth", 2))
mom_rat = Character("Momma Rat", 15, Weapon("Slime", 5), Armor("Big rat hide", 5))
baby_giant = Character("Baby Giant", 20, Weapon("Hand", 7), Armor("Skin", 10))
child_giant = Character("Child Giant", 22, Weapon("Hand", 8), Armor("Skin", 11))
teen_giant = Character("Teenager Giant", 24, Weapon("Hand", 9), Armor("Skin", 12))
adult_giant = Character("Adult Giant", 26, Weapon("Hand", 10), Armor("Skin", 13))
elder_giant = Character("Elder Giant", 30, Weapon("Hand", 12), Armor("Skin", 14))

# Room instantiation
# Forest
FSTART = Room("Forest Start",
              "The beginning of your journey, where it all begins. There's trees around you as far as the eye can see, "
              "and right above you the trees open up to allow a ray of sunshine to shine onto a pentagram that you are "
              "standing on. You have no thoughts, no memories except for one aching command: 'Murder the giants.'",
              'F1', 'F2', 'F3', 'F4', None, None, [Healthpotion()])
F1 = Room("Forest Clearing", "There was a mutated rat you fought here because the dev wasn't lazy anymore! There's "
                             "paths in all directions.", 'F14', 'F2', 'FSTART', 'F4', None, None, None, m_rat)
F2 = Room("Forest Clearing", "There's paths in all directions.", 'F1', 'F5', 'F3', 'FSTART', None, None, None, m_rat)
F3 = Room("Forest Clearing", "There's paths in all directions", 'FSTART', 'F2', 'F7', 'F4', None, None, None, m_rat)
F4 = Room("Forest Clearing", "There's paths in all directions.", 'F1', 'FSTART', 'F3', 'F10', None, None, None, m_rat)
F5 = Room("A calm forest clearing", "You look around and feel an odd sense of calm here, as if you're safe for now. "
                                    "There's paths to the East and West.", None, 'F6', None, 'F2', None, None,
          [Healthpotion()])
F6 = Room("A dead end.", "A giant, wide tree blocks your path forward. Luckily a giant stick lies on the ground that "
                         "looks just big \nenough for you to swing like a weapon. You can exit to the West.", None,
          None, None, 'F5', None, None, [Makeshiftsword()])
F7 = Room("Forest clearing", "There's paths to the North and to the South.", 'F3', None, 'F8', None, None, None,
          None, m_rat)
F8 = Room("Mutated Rat Den",
          "A disgustingly polluted rat den, filled with multiple dead rats."
          "\n In the center of the room there was a giant, bulging rat blob spewing more pollution and"
          "\ndying rat babies. You felt a strong urge to purge this beast from this world, and so you did. You may now "
          "exit either to the North or the South", 'F7', None, 'F9', None, None, None, None, mom_rat)
F9 = Room("Dead End #2: Electric Boogaloo",
          "It's yet another dead end, or your first depending on what path you've taken now. You notice" 
          "\nsome weird armor of questionable origin, which is covered in the polluted goop the rat den" 
          "\n behind you continuously spews out. You can exit to the North.", 'F8', None, None, None, None, None,
          [Makeshiftarmor()])
F10 = Room("Faerie forest clearing entrance", "There's an ominous entrance to a more mystical, wondrous part of the"
                                              "\nforest, some tiny voices beckon you inward. There's paths to the East "
                                              "and the West.", None, 'F4', None, 'F11')
F11 = Room("Faerie forest clearing", "You can go deeper North into the faerie forest or you can exit it to the East.",
           'F12', 'F10', None, None, None, None, None, fairy)
F12 = Room("Faerie forest clearing", "You can go deeper East into the forest or turn back and head South.", None,
           'F13', 'F11', None, None, None, None, fairy)
F13 = Room("Faerie forest clearing", "You can go deeper South into the forest or turn back and start to leave West.",
           None, None, 'FS', 'F12', None, None, None, fairy)
FS = Room("Faerie sword clearing", "After murdering several faeries you walk into an uncharacteristicly calm clearing "
                                   "\nwith a sword that's been forced into a large rock slab in the middle of it. "
                                   "\nA beam of light shines brightly upon the blade, making it shine in the "
                                   "\nlight of its own glory. You can exit to the North.", 'F13', None, None, None,
          None, None, [Ironsword()])
F14 = Room("A calm forest crossroads",
           "You look around and feel an odd sense of calm here, as if you're safe for now. A signpost in the middle of "
           "\nthe road points in the four cardinal directions, with labels for each."
           "\nNorth: Another crossroads,"
           "\nEast: Strange Faerie Man Wannabe's Home and shop, and Piggy Fountain,"
           "\nSouth: Forest clearing,"
           "\nWest: Locked up Cultist's cave.", 'F17', 'F15', 'F1', None)
F15 = Room("Faerie Man's Home (Outside)", "The outside of the weird Faerie wannabe man's home. It smells of cream "
                                          "cheese and loneliness. His home also doubles as a small shop, which he has "
                                          "left unattended. You can go East and South.", None, 'F16', None, 'F14', None,
           None, [Healthpotion()])
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
                              "haphazardly that you can't pick up, as it is simply painted onto the ground. You "
                              "can return to the crossroads by heading East.", None, 'F17', None, None, None, None,
           [Disappointment()])
# Forest Tower
TSTART = Room("The First Floor of a Very Tall Tower", "A Baby Giant slumbers eternally here.",
              None, None, None, None, 'T1', 'TB', None, baby_giant)
TB = Room("The Tower Basement", "You can barely see in front of yourself because of how dark it is in here.", None,
          None, None, None, 'TSTART')
T1 = Room("The second floor of the Very Tall Tower", "A Child Giant slumbers here eternally.", None, None, None, None,
          'T2', 'T1', None, child_giant)
T2 = Room("The third floor of the Very Tall Tower", "A Teenage Giant slumbers here eternally.", None, None, None, None,
          'T3', 'T1', None, teen_giant)
T3 = Room("The fourth floor of the Very Tall Tower", "An Adult Giant sleeps here eternally.", None, None, None, None,
          'T4', 'T2', None, adult_giant)
T4 = Room("The roof of the Very Tall Tower",
          "As they breath their final breath, The Last Giant says to you: \"Please, demon... Avenge my race."
          "Take this key and murder the cultists that summoned you to cull the last of our people, please...\""
          "You take your sword and plunge it into him a final time."
          "\nAs the life leaves his eyes you pick up the key and turn it in your hand as you think about what he said, "
          "his words echoing through your mind.",
          None, None, None, None, None, 'T3', [Gianthand(), Giantsheart(), Giantskin(), Cavekey()], elder_giant)
# Ominous Cave
CSTART = Room("Ominous cave entrance",
              "The entrance to a damp, smelly cave. You hear chants in the distance and see what appears to be a small "
              "shop ahead of you, past a very tall ladder that reaches far into the cave's y axis.", None, 'F14',
              None, 'C1')
C1 = Room("The bottom of a large ladder", "You stare up the large ladder and hear the chanting faintly, the rungs "
                                          "beckoning you to grasp and climb them.", None, 'CSTART', None, 'CSHOP',
          'C2')
CSHOP = Room("A rogue cultist's shop", "A small, humble shop set up by a former cultist. You can't buy anything yet, "
                                       "but he sure does exist.", None, 'C1', None, 'C9')
C2 = Room("Ladder part 1", "What a thrill... \nWith darkness and silence through the night...", None, None, None, None,
          'C3', 'C1')
C3 = Room("Ladder part 2: Electric Boogaloo", "What a thrill... \nI'm searching and I'll melt into you...", None, None,
          None, None, 'C4', 'C2')
C4 = Room("Ladder part 3: The Climb Continues", "What a fear in my heart... But you're so supreme!", None, None, None,
          None, 'C5', 'C3')
C5 = Room("Ladder part 4: This reference is still going", "I give my life, not for honor, but for you! (Snake Eater) "
                                                          "\nIn my time, there'll be no one else...", None, None, None,
          None, 'C6', 'C4')
C6 = Room("Ladder part 5: The Final Rung", "Crime, it's the way I fly to you! (Snake Eater)"
                                           "\nI'm still in a dream, Snake Eater...", None, None, None, 'C7', None, 'C5')
C7 = Room("Cultist's hallway", "A single cultist stands here, frozen because I still do not have a battle system coded "
                               "yet.", None, 'C6', None, 'C8')
C8 = Room("The cultist's lair", "The cultists are chanting to summon a demon. They're all frozen though because that "
                                "battle system still isn't in place yet, sorry.", None, 'C7')
C9 = Room("A patch of gravel", "It's a small patch of gravel behind the Rogue Cultist's shop. \nIt feels loose somehow"
                               ", but no matter how hard you step or jump on it, it doesn't give way to whatever is "
                               "beneath it.", None, 'CSHOP')
# The Pit
PSTART = Room("The bottom of The Pit", "You willingly fall down the large hole and land on a soft patch of... bones."
                                       "\nYeah, you're starting to see why this place was covered up.", None, 'P1',
              None, None, None, 'PB')
PB = Room("Pit pit", "A small pit within in the pit. There seems to be a piece of shiny metal here, too.", None, None,
          None, None, 'PSTART')
P1 = Room("Crazed hobo's squatting spot", "A crazed hobo sits here, waving a spork at you while he clutches a can "
                                          "of beans. \nOther than that though, he's frozen, since I still don't have a "
                                          "freaking battle system.", None, 'P2', None, 'PSTART')
P2 = Room("A shotgun...?", "A Sentient Shotgun floats here, yelling at you various horrible things."
                           "\nIt too is frozen, for it's creator still hath not coded upon him a way to express his "
                           "rage."
                           "express his rage.", None, 'P3', None, 'P1')
P3 = Room("A portal out", "A one-way portal back up to the Rogue Cultist's shop.", None, None, None, 'P2', 'CSHOP')
# Win room
WIN_ROOM = Room("The last room.", "A giant cave full of various treasures! Congrats, you won!", None, None, None, None,
                None, 'P8')

player = Player(FSTART)

directions = ['north', 'east', 'south', 'west', 'up', 'down']
short_directions = ['n', 'e', 's', 'w', 'u', 'd']
playing = True
print("NOTE: You cannot use items or fight any enemies yet, sorry.")
print("-" * 20)

# Controller
while playing and YouVars.health > 0:

    if player.current_location.enemies is not None:
        fight(player.current_location.enemies)

    print(player.current_location.name)
    print("-" * 20)
    print(player.current_location.description)
    print("-" * 20)

    if len(player.current_location.items) > 0:
        print("The following items are in the room:")
        for item in player.current_location.items:
            print(item.name)

    command = input(">_")
    if command.lower() in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    if command.lower() in ('q', 'quit', 'exit'):
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("You're unable to go this way, and now your nose hurts from running into an invisible wall.")
            YouVars.health -= 1
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
            print("You don't have one, you freaking fool.")
    elif 'use' in command.lower():
        item_to_use = command[4:]

        try:
            item = player.find_item(item_to_use)
            if item is None:
                raise AttributeError
            player.use(item)
        except AttributeError:
            print("You either cannot use this item or you do not have it. Either way you are WRONG.")
    elif 'take off' in command.lower():
        item_to_unequip = command[8:]

        try:
            item = player.find_item(item_to_unequip)
            if item is None:
                raise AttributeError
            player.unequip(item)
        except AttributeError:
            print("You don't have one equipped in the first place, you illiterate fool.")
    elif 'pick up' in command.lower():
        item_to_take = command[7:]

    elif 'help' in command.lower():
        print("You can say 'pick up' to pick up all items in a room."
              "\n When in a battle the only option is to say 'attack' if you do anything else you will be damaged."
              "\n You can press enter or type in 'i' to view your inventory."
              "\n You can type in 'use' to use consumables in your inventory, but make sure to capitalize them "
              "properly!"
              "\n You can also type in 'equip' to equip any weapons or armor you have in your inventory!"
              "\n The Ominous Cave is unfinished, but I hope you enjoy it anyways!")

        try:
            if len(player.current_location.items) < 0:
                raise AttributeError
            player.pick_up()
        except AttributeError:
            print("There is no item to pick up here, you blind fool.")
    elif 'inventory' or 'i' in command.lower():
        player.view_inventory()
    else:
        print("Command not recognized.")
