# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    """Room docstring"""

    def __init__(self, name, description, n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.items = []

    def __str__(self):
        return f'{self.name} {self.description}'

    def displayItems(self):
        for item in self.items:
            print(item)

    def addItems(self, *newItems):
        for item in newItems:
            self.items.append(item)

    def dropItems(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} can not be dropped in this room ')
