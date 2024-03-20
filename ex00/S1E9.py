from abc import ABC, abstractmethod


class Character(ABC):
    """Docstring for class Character"""

    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Docstring for Constructor of class Character"""
        self.name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Docstring for method die of class Character"""
        pass


class Stark(Character):
    """Docstring for class Stark"""

    def __init__(self, name, is_alive=True):
        """Docstring for Constructor of class Stark"""
        super().__init__(name, is_alive)

    def die(self):
        """Docstring for method die of class Stark"""
        self.is_alive = False
