from plateau import Plateau

class Rover:
    """ Rover class, representing a robotic rover sended by NASA to mars. """
    def __init__(self, position_x: int, position_y: int, face_direction: str, plateau):
        self.plateau = plateau
        self.position_x = position_x
        self.position_y = position_y
        self.face_direction = face_direction

    @property
    def plateau(self):
        return self.__plateau

    @plateau.setter
    def plateau(self, plateau):
        if isinstance(plateau, Plateau):
            self.__plateau = plateau
        else:
            raise ValueError(f"Wrong plateau setter, value informed: {plateau}")

    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, position_x):
        validation = self.position_validation_x(position_x)
        if validation:
            self.__position_x = position_x
        else:
            raise ValueError(f"Wrong value setter, value informed: {position_x}")

    @property
    def position_y(self):
        return self.__position_y

    @position_y.setter
    def position_y(self, position_y):
        validation = self.position_validation_y(position_y)
        if validation:
            self.__position_y = position_y
        else:
            raise ValueError(f"Wrong value setter, value informed: {position_y}")

    @property
    def face_direction(self):
        return self.__face_direction

    @face_direction.setter
    def face_direction(self, face_direction):
        possibles_faces = ['N', 'S', 'E', 'W']
        if face_direction.isalpha() and face_direction.upper() in possibles_faces \
            and isinstance(face_direction, str):
            self.__face_direction = face_direction
        else:
            raise ValueError(f"Wrong value setter, value informed: {face_direction}")

    def position_validation_x(self, position):
        try:
            if isinstance(position, int) and position >= self.__plateau.min_x and \
                position <= self.__plateau.max_x:
                return True
            else:
                return False
        except ValueError:
            raise ValueError(f"Wrong value setter, value informed: {position}")

    def position_validation_y(self, position):
        try:
            if isinstance(position, int) and position >= self.__plateau.min_y and \
                position <= self.__plateau.max_y:
                return True
            else:
                return False
        except ValueError:
            raise ValueError(f"Wrong value setter, value informed: {position}")
