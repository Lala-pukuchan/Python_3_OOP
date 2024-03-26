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


class Stark(Character):
    """Docstring for class Stark"""

    def __init__(self, first_name, is_alive=True):
        """Docstring for Constructor of class Stark"""
        super().__init__(first_name, is_alive)


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)


if __name__ == "__main__":
    main()
