from S1E9 import Character


class Baratheon(Character):
    """Docstring for class Baratheon"""

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


# class Lannister(Character): #your code here
## decorator
# def create_lannister(your code here): #your code here
