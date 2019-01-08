class Plateau:
    """ Plateau class, representing the 'map' that rovers will land and explore."""
    def __init__(self, max_x: int, max_y: int):
        self.__max_x = max_x
        self.__max_y = max_y
        self.__min_x = 0
        self.__min_y = 0

    @property
    def max_x(self):
        return self.__max_x

    def __str__(self):
        return f"Max Values: ({self.__max_x},{self.__max_y}) \nMin Values: ({self.__min_x}, {self.__min_y})"


if __name__ == '__main__':
    pla = Plateau('STR', 5)
    print(pla)
    print(pla.max_x)
    print(type(pla))
    print(type(pla.max_x))
