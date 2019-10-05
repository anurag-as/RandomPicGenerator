import numpy
from PIL import Image
import os


def initialize_matrix(board_size):
    """
    Initialize image matrix of pixels
    :param board_size: Size of board
    :return: data matrix
    """
    data = numpy.zeros((board_size, board_size, 3), dtype=numpy.uint8)
    return data


def form_image(data):
    """
    Form the image from the pixels
    :param data: data pixels
    :return: Image
    """
    image = Image.fromarray(data)
    return image


def show_image(image):
    """
    Function to display the image
    :param image: Image object (PIL)
    :return: None
    """
    image.show()


def next_path(path_pattern):
    i = 1
    while os.path.exists(path_pattern % i):
        i = i * 2
    a, b = (i // 2, i)
    while a + 1 < b:
        c = (a + b) // 2
        a, b = (c, b) if os.path.exists(path_pattern % c) else (a, c)
    return path_pattern % b


def save_image(image):
    """
    Save the image in jpg format
    :param image: Image object (PIL)
    :return: None
    """
    file_name = next_path(".//images//random_art_%s.jpg")
    image.save(file_name, "JPEG")
    return file_name