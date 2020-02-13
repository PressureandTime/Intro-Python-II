# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        # self.s_to = s_to
        # self.n_to = n_to
        # self.w_to = w_to
        # self.e_to = e_to
        self.items = items

    def print_all_items(self):
        if len(self.items) > 0:
            all_items = [item.name for item in self.items]
            print(f"items that are current: {all_items} in {self.name}")
        else:
            print(f"there are no items in {self.name}")

    def remove_the_item(self, item):
        for thing in self.items:
            if item == thing:
                self.items.remove(item)
                print(f"{item} has been removed")
            elif item not in self.items:
                print('item was not found')

    def add_the_item(self, item):
        self.items.append(item)
