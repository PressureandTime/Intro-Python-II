# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room):
        self.room = room
        self.inventory = []

    def way_to_go(self, d):
        print(d)

    def add_the_item(self, item):
        self.inventory.append(item)

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


conan = Player('field')

conan.add_the_item('sword')
conan.add_the_item('shield')
conan.add_the_item('axe')

print(vars(conan))

conan.remove_the_item('shield')
print(vars(conan))

conan.print_all_items()

