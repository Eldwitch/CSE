world_map = {
    'FSTART': {
        'NAME': "Forest Start",
        'DESCRIPTION': "The beginning of your journey, where it all began. There's trees around you as far as the eye"
                       "\n can see, and right above you the trees open up to allow a ray of sunshine to shine onto a"
                       "\n pentagram you stand on.",
        'PATHS': {
            'NORTH': "F1",
            'EAST': "F2",
            'SOUTH': "F3",
            "WEST": "F4"
        }
    },
    'F1': {
        'NAME': "Forest clearing",
        'DESCRIPTION': "There's a mutated rat you cannot fight yet here because the dev is lazy",
        'PATHS': {
            'SOUTH': "FSTART",
            'NORTH': "F14",
            'EAST': "F2",
            "WEST": "F4"
        }
    },
    'F2': {
        'NAME': "Forest clearing",
        'DESCRIPTION': "There's a mutated rat you cannot fight yet here because the dev is lazy",
        'PATHS': {
            'NORTH': "F1",
            'EAST': "F5",
            'SOUTH': "F3",
            "WEST": "FSTART"
        }
    },
    'F3': {
        'NAME': "Forest clearing",
        'DESCRIPTION': "There's a mutated rat you cannot fight yet here because the dev is lazy",
        'PATHS': {
            'NORTH': "FSTART",
            'EAST': "F2",
            'SOUTH': "F7",
            "WEST": "F4"
        }
    },
    'F4': {
        'NAME': "Forest clearing",
        'DESCRIPTION': "There's a mutated rat you cannot fight yet here because the dev is lazy",
        'PATHS': {
            'NORTH': "F1",
            'EAST': "FSTART",
            'SOUTH': "F3",
            "WEST": "F10"
        }
    },
    'F5': {
        'NAME': "A calm forest clearing",
        'DESCRIPTION': "You look around and feel an odd sense of calm here, as if you're safe for now.",
        'PATHS': {
            'EAST': "F6",
            "WEST": "F2"
        }
    },
    'F6': {
        'NAME': "A dead end.",
        'DESCRIPTION': "A giant, wide tree blocks your path forward. Luckily a giant stick lies on the ground that"
                       "\n looks just big enough for you to swing like a weapon.",
        'PATHS': {
            "WEST": "F5"
        }
    },
    'F7': {
        'NAME': "Forest clearing",
        'DESCRIPTION': "There's a mutated rat you cannot fight yet here because the dev is STILL too lazy",
        'PATHS': {
            'NORTH': "F3",
            'SOUTH': "F8"
        }
    },
    'F8': {
        'NAME': "Mutated rat den",
        'DESCRIPTION': "A disgustingly polluted rat den, filled with multiple dead rats and barely alive rat babies."
                       "\n In the center of the room there's a giant, bulging rat blob spewing more pollution and"
                       "\n dying rat babies. You feel a strong urge to purge this beast from this world. Sadly, the"
                       "\n fight system isn't implemented yet, so you are forced to move along in utter disgust.",
        'PATHS': {
            'NORTH': "F7",
            'SOUTH': "F9"
        }
    },
    'F9': {
        'NAME': "Dead End #2: Electric Boogaloo",
        'DESCRIPTION': "It's yet another dead end, or your first depending on what path you've taken now. You notice"
                       "\n some weird armor of questionable origin, which is covered in the polluted goop the rat den"
                       "\n behind you spews out.",
        'PATHS': {
            'NORTH': "F8"
        }
    },
    'F10': {
        'NAME': "Fairy forest clearing entrance",
        'DESCRIPTION': "There's an ominous entrance to a more mystical, wondrous part of the forest, some tiny voices"
                       "\n beckon you inward.",
        'PATHS': {
            'EAST': "F4",
            "WEST": "F11"
        }
    },
    'F11': {
        'NAME': "Faerie forest clearing",
        'DESCRIPTION': "There's a Faerie you cannot fight yet here because the dev is lazy",
        'PATHS': {
            'NORTH': "F12",
            'EAST': "F10"
        }
    },
    'F12': {
        'NAME': "Faerie forest clearing",
        'DESCRIPTION': "There's another Faerie you cannot fight yet here because the dev is still lazy",
        'PATHS': {
            'EAST': "F13",
            'SOUTH': "F11"
        }
    },
    'F13': {
        'NAME': "Faerie forest clearing",
        'DESCRIPTION': "There's yet another Faerie you cannot fight yet here because the dev is still too lazy",
        'PATHS': {
            'SOUTH': "FS",
            "WEST": "F12"
        }
    },
    'FS': {
        'NAME': "Faerie sword clearing",
        'DESCRIPTION': "After murdering several faeries you walk into an uncharacteristicaly ",
        'PATHS': {
            'NORTH': "F13"
        }
    },
}

# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map['FSTART']  # This is your current location
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
            print("A giant hand comes from the sky and turns you away from this path before promptly disappearing.")
    else:
        print("Command not recognized.")
