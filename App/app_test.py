import pytest


@pytest.fixture
def data():
    return {"data": "5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM",}


@pytest.fixture
def Plateau():
    from plateau import Plateau
    return Plateau


@pytest.fixture
def Rover():
    from rover import Rover
    return Rover


@pytest.fixture
def Transform(data):
    from transform import Transform
    return Transform


# Plateau Tests Below

def test_plateau_correct_data_sample_one(Plateau):
    plateau = Plateau(5, 5)
    assert plateau.max_x == 5
    assert plateau.max_y == 5
    assert plateau.min_x == 0
    assert plateau.min_y == 0


def test_plateau_correct_data_sample_two(Plateau):
    plateau = Plateau(10, 12)
    assert plateau.max_x == 10
    assert plateau.max_y == 12
    assert plateau.min_x == 0
    assert plateau.min_y == 0


def test_plateau_with_wrong_data_sample_with_string_in_y(Plateau):
    with pytest.raises(ValueError):
        plateau = Plateau(10, 'ST')


def test_plateau_with_wrong_data_sample_with_string_in_x(Plateau):
    with pytest.raises(ValueError):
        plateau = Plateau('sr', 12)


def test_plateau_with_wrong_data_sample_with_empty_string(Plateau):
    with pytest.raises(ValueError):
        plateau = Plateau('', 12)


def test_plateau_with_wrong_data_sample_with_empty_list(Plateau):
    with pytest.raises(TypeError):
        plateau = Plateau(1, [])


# Rover Tests Below

def test_stoped_rover_with_correct_data_sample_one(Rover, Plateau):
    plat = Plateau(5, 5)
    rover = Rover(1, 2, 'N', plat)
    assert rover.position_x == 1
    assert rover.position_y == 2
    assert rover.face_direction == 'N'
    assert plat.max_x == 5
    assert plat.max_y == 5


def test_stoped_rover_with_correct_data_sample_two(Rover, Plateau):
    plat = Plateau(10, 12)
    rover = Rover(3, 3, 'E', plat)
    assert rover.position_x == 3
    assert rover.position_y == 3
    assert rover.face_direction == 'E'
    assert plat.max_x == 10
    assert plat.max_y == 12


def test_rover_with_wrong_position_y(Plateau, Rover):
    with pytest.raises(ValueError):
        plateau = Plateau(10, 'ST')
        rover = Rover(3, 'S', 'E', plateau)

def test_rover_with_wrong_position_x(Plateau, Rover):
    with pytest.raises(ValueError):
        plateau = Plateau(10, 'ST')
        rover = Rover('E', 5, 'E', plateau)

def test_rover_with_wrong_face_direction(Plateau, Rover):
    with pytest.raises(ValueError):
        plateau = Plateau(10, 'ST')
        rover = Rover(3, 6, 7, plateau)

def test_rover_wich_exceeds_value_of_x(Plateau, Rover):
    with pytest.raises(ValueError):
        plateau = Plateau(10, 12)
        rover = Rover(11, 11, 'E', plateau)

def test_rover_wich_exceeds_value_of_y(Plateau, Rover):
    with pytest.raises(ValueError):
        plateau = Plateau(10, 5)
        rover = Rover(10, 7, 'E', plateau)


# Changing Directions tests

def test_if_face_was_correctly_changed_to_right(Rover, Plateau):
    plat = Plateau(5, 5)
    rover = Rover(1, 2, 'N', plat)
    rover.change_position('R')
    assert rover.face_direction == 'E'
    rover.change_position('R')
    assert rover.face_direction == 'S'


def test_if_face_was_correctly_changed_to_left(Rover, Plateau):
    plat = Plateau(5, 5)
    rover = Rover(1, 2, 'N', plat)
    rover.change_position('L')
    assert rover.face_direction == 'W'
    rover.change_position('L')
    assert rover.face_direction == 'S'


def test_if_face_was_correctly_changed_to_both_sides(Rover, Plateau):
    plat = Plateau(5, 5)
    rover = Rover(1, 2, 'N', plat)
    rover.change_position('R')
    assert rover.face_direction == 'E'
    rover.change_position('L')
    assert rover.face_direction == 'N'
    rover.change_position('L')
    rover.change_position('L')
    assert rover.face_direction == 'S'


# Moving Robotics rover tests

def test_if_rover_was_correctly_moved_north(Rover, Plateau):
    plat = Plateau(5, 5)
    rover = Rover(1, 2, 'N', plat)
    rover.change_position('M')
    assert rover.position_y == 3
    rover.change_position('M')
    assert rover.position_y == 4


def test_if_rover_was_correctly_moved_south(Rover, Plateau):
    plat = Plateau(5, 5)
    rover = Rover(1, 3, 'S', plat)
    rover.change_position('M')
    assert rover.position_y == 2
    rover.change_position('M')
    assert rover.position_y == 1


def test_if_rover_was_correctly_moved_west(Rover, Plateau):
    plat = Plateau(5, 5)
    rover = Rover(3, 3, 'W', plat)
    rover.change_position('M')
    assert rover.position_x == 2
    rover.change_position('M')
    assert rover.position_x == 1


def test_if_rover_was_correctly_moved_east(Rover, Plateau):
    plat = Plateau(5, 5)
    rover = Rover(3, 3, 'E', plat)
    rover.change_position('M')
    assert rover.position_x == 4
    rover.change_position('M')
    assert rover.position_x == 5


def test_if_rover_was_correctly_moved_over_boundary(Rover, Plateau):
    plat = Plateau(5, 5)
    rover = Rover(1, 2, 'N', plat)
    rover.change_position('M')
    assert rover.position_y == 3
    rover.change_position('M')
    assert rover.position_y == 4
    rover.change_position('M')
    rover.change_position('M')
    rover.change_position('M')
    assert rover.position_y == 5
    assert rover.position_x == 1


# Final Test Assertion

def test_final(data, Transform):
    output = Transform().transform(data)
    assert output == "1 3 N\n5 1 E\n"
