class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take_the_item(self):
        print(f"you have picked up {self.name}")

    def drop_the_item(self):
        print(f"You dropped the {self.name}")
