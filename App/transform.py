from rover import Rover
from plateau import Plateau

class Transform:

    def transform(self, data):
        x, y = self.__get_plateau_x_y(data)
        plato = Plateau(x, y)

        new_data = self.__transform_data(data)
        rovers_output = ''
        for i in range(0, len(new_data), 2):
            data_splited = new_data[i].split(' ')
            position_x, position_y = data_splited[0], data_splited[1]
            face_direction = data_splited[2]
            new_rover = Rover(position_x, position_y, face_direction, plato)
            output = self.__move_rover(new_rover, new_data[i + 1])
            rovers_output += output
        return rovers_output


    def __get_plateau_x_y(self, data):
        new_data = data['data'].split('\n')
        x, y = new_data[0].split(' ')
        return int(x), int(y)


    def __transform_data(self, data):
        new_data = data['data'].split('\n')
        return new_data[1:]


    def __move_rover(self, rover, data):
        for letter in data:
            rover.change_position(letter)
        output_string = f"{rover.position_x} {rover.position_y} {rover.face_direction}\n"
        return output_string


if __name__ == '__main__':
    data = {"data": "5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"}
    output = Transform().transform(data)
    print(output)
