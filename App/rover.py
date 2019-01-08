class Rover:
    """ Rover class, representing a robotic rover sended by NASA to mars. """
    def __init__(self, position_x: int, position_y: int, face_direction: int, plateau: Plateau):
        self.validation(position_x, position_y, face_direction, plateau)
        self.position_x = position_x
        self.position_y = position_y
        self.face_direction = face_direction
        self.plateau = plateau

    def validation(self, position_x, position_y, face_direction, plateau) -> bool:
        pass
