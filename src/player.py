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
        print('item was not found')


conan = Player('field')

conan.add_the_item('sword')
conan.add_the_item('shield')
conan.add_the_item('axe')

print(vars(conan))

conan.remove_the_item('shield')
print(vars(conan))
