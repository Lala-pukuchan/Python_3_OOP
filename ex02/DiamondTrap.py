from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    King class
    """

    def __init__(self, name):
        super().__init__(name)

    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, color):
        self.hairs = color

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")


if __name__ == "__main__":
    main()
