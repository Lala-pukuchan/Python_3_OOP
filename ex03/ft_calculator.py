import numpy as np


class calculator:

    def __init__(self, value):
        self.value = np.array(value)

    def __add__(self, object) -> None:
        self.value = self.value + object
        print(self.value)
        return self.value

    def __mul__(self, object) -> None:
        self.value = self.value * object
        print(self.value)
        return self.value

    def __sub__(self, object) -> None:
        self.value = self.value - object
        print(self.value)
        return self.value

    def __truediv__(self, object) -> None:
        if object == 0:
            print("division by zero")
            return
        self.value = self.value / object
        print(self.value)
        return self.value


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5


if __name__ == "__main__":
    main()
