# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def set_the_room(self, current_room):
        self.room = current_room

    def add_the_item(self, item):
        self.inventory.append(item)
        print(f"you took the {item} and stashed into your inventory")

    def remove_the_item(self, item):
        for thing in self.inventory:
            if item == thing:
                self.inventory.remove(item)
                print(f"{item} has been removed")
            elif item not in self.inventory:
                print('item was not found')

    def print_all_items(self):
        if len(self.inventory) > 0:
            all_items = [item for item in self.inventory]
            print(f"inventory contents: {all_items}")
        else:
            print(f"your inventory is empty")
