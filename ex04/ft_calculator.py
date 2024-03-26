import numpy as np


class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print("Dot product is:", np.dot(V1, V2))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print("Add Vector is :", np.add(V1, V2))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print("Sous Vector is:", np.subtract(V1, V2))
