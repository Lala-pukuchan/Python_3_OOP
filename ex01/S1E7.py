from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(
        self,
        first_name,
        is_alive=True,
        family_name="Baratheon",
        eyes="brown",
        hairs="dark",
    ):
        """Representing the Baratheon family."""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(
        self,
        first_name,
        is_alive=True,
        family_name="Lannister",
        eyes="blue",
        hairs="light",
    ):
        """Representing the Lannister family."""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """create instance of Lannister family."""
        instance = cls(first_name, True)
        instance.is_alive = is_alive
        return instance


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)


if __name__ == "__main__":
    main()
