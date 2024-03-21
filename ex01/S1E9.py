from abc import ABC, abstractmethod


class Character(ABC):
    """Docstring for class Character"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Docstring for Constructor of class Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Docstring for method die of class Character"""
        self.is_alive = False

    #def __str__(self):
    #    return f"Vector({self.family_name}, {self.eyes}, {self.hairs})"

    #def __repr__(self):
    #    return self.__str__()


class Stark(Character):
    """Docstring for class Stark"""

    def __init__(self, first_name, is_alive=True):
        """Docstring for Constructor of class Stark"""
        super().__init__(first_name, is_alive)
