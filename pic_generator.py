import random


def number_random(size):
    """
    Generate number of random blocks
    :param size: Side of an image, number of segments
    :return: Number of random coloured blocks
    """
    blocks = size ** 2
    number = random.randint(0, blocks)
    return number


def particular_blocks(number, size):
    """
    Random blocks which must be coloured
    :param number: Number of random blocks
    :param size: Board size
    :return: Positions of the random blocks
    """
    return random.sample(range(size**2), number)


def one_two(oned, size):
    """
    Converting 1Dimensional number to 2Dimensional number
    :param oned: 1Dimensional Number
    :param size: Size of board
    :return: 2Dimensional number
    """
    x_coordinate = oned // size
    y_coordinate = (oned % size)
    position = (x_coordinate, y_coordinate)
    return position


def block_coordinates(sequence, size):
    """
    Get 2Dimensional Coordinates for all the random sequences
    :param sequence: List of 1D random numbers
    :param size: Board or array dimension
    :return: Tuples of 2D positions
    """
    positions = set()
    for block in sequence:
        positions.add(one_two(block, size))
    return positions
