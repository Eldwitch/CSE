class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, east=None, south=None, west=None, up=None, down=None, floor=None):
        self.name = name
        self.floor = floor
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down


# These are the instances of the rooms (Instantiation)

# Option 1 - Use the variables, but fix later
R19A = Room("Mr. Wiebes Room")
parking_lot = Room("The Parking Lot", None, R19A)
R19A.north = parking_lot

# Option 2 - Use strings, but more difficult controller
R19A = Room("Mr. Wiebes Room", 'parking_lot')
parking_lot = Room("The Parking Lot", None, "R19A")
