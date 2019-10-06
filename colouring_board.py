from utils.testing_board import *
from utils.board_size_choose import *
from utils.pic_generator import *
import pymsgbox
import random

"""
Colour list
Olive - [40, 250, 106], Light Blue - [66, 140, 252], Dark Blue - [0, 13, 255]
Purple - [140, 0, 255], Baby Pink - [255, 92, 247], Light Red - [255, 92, 92]
Red - [255, 0, 0], Grey - [97, 85, 85], Dark Green - [70, 77, 2]
Green Blue - [0, 255, 179]

"""
colours = [[40, 250, 106], [66, 140, 252], [0, 13, 255], [140, 0, 255], [255, 92, 247], [255, 92, 92],
           [255, 0, 0], [70, 77, 2], [0, 255, 179]]
default_colours = {'peach': [255, 251, 143]}


def randomize_colour():
    """
    Randomize the forward colour in the image
    :return: Index of the colour
    """
    return random.randint(0, len(colours)-1)


def colour_board(image_data, block_coords, board, interval_size):
    """
    Colour the image based on randomness
    :param image_data: Image matrix
    :param block_coords: Blocks where colour is different from the background
    :param board: Board size
    :param interval_size: Interval for colour changing
    :return: Coloured image
    """
    random_colour = randomize_colour()
    for i in range(board):
        for j in range(board):
            image_data[i][j] = default_colours['peach']
    for block in block_coords:
        for x in range(block[0]*interval_size, (block[0]*interval_size)+interval_size):
            for y in range(block[1]*interval_size, (block[1]*interval_size)+interval_size):
                image_data[x][y] = colours[random_colour]
    return image_data


if __name__ == "__main__":
    while True:
        try:
            input_size = int(pymsgbox.prompt('Image size?', default='5'))
            break
        except ValueError:
            pymsgbox.alert("Error, please input a valid size")
    board_size = choose_board_size(input_size)
    intervals = get_intervals(board_size, input_size)
    data = initialize_matrix(board_size)
    number = number_random(input_size)
    blocks = particular_blocks(number, input_size)
    block_coordinate = block_coordinates(blocks, input_size)
    coloured_data = colour_board(data, block_coordinate, board_size, intervals)
    formed_image = form_image(coloured_data)
    show_image(formed_image)
    filename = save_image(formed_image)
    print("Image has been saved in images folder as %s" % filename)
