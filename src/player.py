# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """Player docstring"""

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

        self.items = []

    def __str__(self):
        return f'{self.current_room}'

    # def displayItemsRoom(self):

    # def displayPlayerItems(self):

    # def addItem(self, item):

    # def dropItem(self, item)
