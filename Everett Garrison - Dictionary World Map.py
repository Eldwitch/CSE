world_map = {
    'R19A': {
        'NAME': "Mr. Wiebes' room",
        'DESCRIPTION': "This is the room that you are in.",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "A Parking Lot",
        'DESCRIPTION': "There are a few cars parked here.",
        'PATHS': {
            'SOUTH': "R19A"
        }
    }
}

# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map['R19A']  # This is your current location
playing = True

# Controller
while playing:
    print(current_node['NAME'])

    command = input(">_")
    if command.lower() in ('q', 'quit', 'exit'):
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")
