class Plateau:
    """ Plateau class, representing the 'map' that rovers will land and explore."""
    def __init__(self, max_x: int, max_y: int):
        self.max_x = max_x
        self.max_y = max_y
        self.__min_x = 0
        self.__min_y = 0

    @property
    def max_y(self):
        return self.__max_y

    @property
    def max_x(self):
        return self.__max_x

    @property
    def min_x(self):
        return self.__min_x

    @property
    def min_y(self):
        return self.__min_y

    @max_x.setter
    def max_x(self, max_x):
        if isinstance(max_x, int) and max_x >= 0:
            self.__max_x = max_x
        else:
            raise ValueError(f"Wrong value setter, value informed: {max_x}")

    @max_y.setter
    def max_y(self, max_y):
        if isinstance(max_y, int) and max_y >= 0 and max_y:
            self.__max_y = max_y
        else:
            raise ValueError(f"Wrong value setter, value informed: {max_y}")

    def __str__(self):
        return f"Max Values: ({self.__max_x},{self.__max_y}) \nMin Values: ({self.__min_x}, {self.__min_y})"


if __name__ == '__main__':
    plat = Plateau(5, 5)
    print(plat)
    plat2 = Plateau(5, 12)
    print(plat2)
    print(type(plat2))
