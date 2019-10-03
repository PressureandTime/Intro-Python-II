class Monster:
    def __init__(self, name):
        self.name = name
        self.level = 22

    def __str__(self):
        return f"{self.name}  level {self.level}"
