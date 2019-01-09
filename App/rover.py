from plateau import Plateau

class Rover:
    """ Rover class, representing a robotic rover sended by NASA to mars. """

    possibles_faces = ['N', 'E', 'S', 'W']
    possibles_coordinates = ['R', 'L', 'M']

    def __init__(self, position_x: int, position_y: int, face_direction: str, plateau):
        self.plateau = plateau
        self.position_x = int(position_x)
        self.position_y = int(position_y)
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
        validation = self.__position_validation_x(position_x)
        if validation:
            self.__position_x = position_x
        else:
            raise ValueError(f"Wrong value setter, value informed: {position_x}")

    @property
    def position_y(self):
        return self.__position_y

    @position_y.setter
    def position_y(self, position_y):
        validation = self.__position_validation_y(position_y)
        if validation:
            self.__position_y = position_y
        else:
            raise ValueError(f"Wrong value setter, value informed: {position_y}")

    @property
    def face_direction(self):
        return self.__face_direction

    @face_direction.setter
    def face_direction(self, face_direction: str):
        if face_direction.isalpha() and face_direction.upper() in Rover.possibles_faces \
            and isinstance(face_direction, str):
            self.__face_direction = face_direction
        else:
            raise ValueError(f"Wrong value setter, value informed: {face_direction}")

    def __position_validation_x(self, position: int):
        try:
            if isinstance(position, int) and position >= self.__plateau.min_x and \
                position <= self.__plateau.max_x:
                return True
            else:
                return False
        except ValueError:
            raise ValueError(f"Wrong value setter, value informed: {position}")

    def __position_validation_y(self, position):
        try:
            if isinstance(position, int) and position >= self.__plateau.min_y and \
                position <= self.__plateau.max_y:
                return True
            else:
                return False
        except ValueError:
            raise ValueError(f"Wrong value setter, value informed: {position}")

    def change_position(self, face: str):
        try:
            face_upper = face.upper()
            if face_upper in Rover.possibles_coordinates:
                if face_upper == 'R':
                    new_position = (Rover.possibles_faces.index(self.face_direction) + 1) % 4
                    self.face_direction = Rover.possibles_faces[new_position]
                elif face_upper == 'L':
                    new_position = (Rover.possibles_faces.index(self.face_direction) - 1) % 4
                    self.face_direction = Rover.possibles_faces[new_position]
                else:
                    self.__movement_calculation()
            else:
                raise ValueError(f"Incorrect face value, value informed: {face}")
        except ValueError:
            raise ValueError(f"Incorrect face value, value informed: {face}")

    def __movement_calculation(self):
        moving = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        x, y = moving[self.face_direction]
        self.__move_one_square(x, y)

    def __move_one_square(self, x, y):
        if self.__position_validation_x(self.position_x + x):
            self.position_x += x
        if self.__position_validation_y(self.position_y + y):
            self.position_y += y
