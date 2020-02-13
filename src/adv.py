from room import Room
from player import Player
from item import Item
import random

# Declare all the rooms

room = {
    'outside':
    Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':
    Room(
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook':
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers."""),
    'empty':
    Room(
        "Empty Room",
        """You walked into an room that seems empty at first glance. To the east is a passage."""
    )
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Conan', room['outside'])

# rabbit_foot = Item("amulet", "this is the amulet that gives luck")

# room[player.room].items.append(rabbit_foot)

item = {
    'axe': Item('axe', 'huge axe'),
    'sword': Item('Sword', 'sharp sword'),
    'shield': Item('Shield', 'bronze shield'),
    'hammer': Item('Hammer', 'heavy hammer')
}

for thing in range(0, 5):
    random_room = random.choice(list(room.keys()))
    random_item = random.choice(list(item.keys()))
    room[random_room].add_the_item(random_item)

end_of_game = False
options = ['n', 'e', 's', 'w']
waypoints = {'n': 'North', 'e': 'East', 's': 'South', 'w': 'West'}
actions = ['get', 'take', 'pick', 'drop', 'check']


def fetch_the_command_from_player():
    return input("Command: ").lower().split(" ")


def move_player(room, command):
    cmd_to = command + '_to'
    if hasattr(room, cmd_to):
        print(f'You move {waypoints[command]}')
        player.set_the_room(getattr(room, cmd_to))
        player.room.where_am_i()
        if player.room.name == 'Treasure Chamber':
            global game_over
            game_over = True
        print('')
    else:
        print('there is nothing here')


while not end_of_game:
    command = fetch_the_command_from_player()
    # command verb, first input
    cmd_v = command[0]

    if cmd_v == 'q':
        game_over = True
    elif cmd_v in options:
        move_player(player.room, cmd_v)
    elif cmd_v == 'i':
        print(player.print_all_items())
    elif cmd_v in actions:
        if cmd_v == 'pick':
            player.add_the_item(item)
        elif cmd_v == 'drop':
            player.remove_the_item(command[1])
        elif cmd_v == 'check':
            player.room.check()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
