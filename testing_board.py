import numpy
from PIL import Image


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


def save_image(image):
    """
    Save the image in jpg format
    :param image: Image object (PIL)
    :return: None
    """
    image.save("image.jpg", "JPEG")
