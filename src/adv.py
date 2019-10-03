from room import Room
from player import Player
from item import Item
from monster import Monster
import textwrap

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}

# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# Main


# helper function


def movePlayer(dir, current_room):
    attrib = dir + "_to"

    # see if room has destination attrib
    if hasattr(current_room, attrib):
        return getattr(current_room, attrib)

    # otherwise let them know that they can not move in  that direction
    print("you cannot go that way")

    return current_room


player = Player("Beowulf", room["outside"])
player.inventory.append(Item("Knife", "a russty knife"))
player.inventory.append(Item("Bracer", "a machine"))
player.inventory.append(Item("Dog", "a fanged dog"))


done = False

while not done:
    print(player.current_room.name)
    print(player.current_room.description)

    s = input("Comand> ").strip().lower()

    if s == "q":
        print("Goodbye")
        done = True
    elif s in ["n", "s", "e", "w"]:
        player.current_room = movePlayer(s, player.current_room)
        if s == "n":
            print(Item("armor", "it looks like its made of steel"))
            answer1 = input("Do you want to pick it up, yes or no?  ").strip().lower()
            if answer1 == "yes":
                print("you placed the armor in your inventory")
                player.inventory.append(
                    Item("armor", "armor that I took in the north room")
                )
            if answer1 == "no":
                print("you decided you not need it")
        if s == "s":
            print(Item("monster", "waiting in ambush to attack you"))
            answer2 = input("Fight it? yes or no  ").strip().lower()
            if answer2 == "yes":
                print("you killed the " + str(Monster("Balrog")))
            if answer2 == "no":
                print("you ran away from the beast")

        if s == "e":
            print(Item("hole", "a giant hole in the ground with no end"))
            input("Jump in it or not?  ").strip().lower()
        if s == "w":
            print(Item("passage", "judging by the breeze it must be an way out"))
            input("Do you want to go there?  ").strip().lower()

    elif s == "i":
        if len(player.inventory) == 0:
            print("you are not carrying anything")
        else:
            print("you are carrying: \n")
            for i in player.inventory:
                print(f"\t{i}")
            print()
    else:
        print(f"the command {s} is not valid!")


# hero = Player("Conan", "outside")
# while True:
#     direction = input("Where do you want to go? (n,s,e,w)  ")
#     print(hero.current_room)
#     if direction == "n":
#         if room[hero.current_room].n_to is not None:
#            hero.current_room = room[hero.current_room].name
#     print(hero.current_room)
# for place in room:
#     foyer = Room("foyer", "Dim light filters in from the south,Dusty passages run north and east.")
#     place = foyer
#     print(place)

# wrapper = textwrap.TextWrapper(width=50)
# word_list = wrapper.wrap(text=direction)
# for element in word_list:
#     print(element)

# Make a new player object that is currently in the 'outside' room.

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
