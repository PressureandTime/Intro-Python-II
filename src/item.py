class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def grab_the_item(self):
        print(f"you have picked up {self.name}")

    def throw_the_item_away(self):
        print(f"You dropped the {self.name}")
