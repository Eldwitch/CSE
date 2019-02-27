class Room(object):
    def __init__(self, name, description, north=None, east=None, south=None, west=None, up=None, down=None, enter=None,
                 floor=None):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.enter = enter
        self.floor = floor
        self.npc = []


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location
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


class Npc(object):
    def __init__(self, name, dialogue="'I am speaking right now.'"):
        self.name = name
        self.dialogue = dialogue


FSTART = Room("Forest Start", "The beginning of your journey, where it all begins. There's trees around you as far as"
                              "\nthe eye can see, and right above you the trees open up to allow a ray of sunshine to"
                              "\nshine onto a pentagram you stand on.", 'F1', 'F2', 'F3', 'F4')
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
           "\nEast: Strange Faerie Man Wannabe's Home and Piggy Fountain, "
           "\nSouth: Forest clearing, West: Blocked up Cave.", 'F17', 'F15', 'F1', None)
F15 = Room("Faerie Man's Home (Outside)", "The outside of the weird Faerie wannabe man's home. It smells of cottage "
                                          "cheese and loneliness.", None, 'F16', None, 'F14')
F16 = Room("Piggy Fountain", "There's a nice sense of calm here as you look at a large fountain ordained with a pig"
                             " spitting a stream of water \ninto a round basin. At the bottom of the basin you can see"
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
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("You're unable to go this way.")
            print("-" * 20)
    else:
        print("Command not recognized.")
