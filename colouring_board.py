from testing_board import *
from board_size_choose import *
from pic_generator import *
import pymsgbox

colours = {'peach': [238, 232, 170], 'olive': [128, 128, 0]}

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
    block_coordinates = block_coordinates(blocks, input_size)
