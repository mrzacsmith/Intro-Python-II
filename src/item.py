class Item:
    """Item docstring"""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickUp(self):
        print(f'You have picked up {self.name}.')


class Food(Item):
    """Food docstring"""

    def __init__(self, name, description, health):
        super().__init__(name, description)
        self.health = health


class Weapon(Item):
    """Weapon docstring"""

    def __init__(self, name, description, damage):
        super().__str__(name, description)
        self.damage = damage
