def choose_board_size(input_size):
    """
    Choose a board size based on input size, which evenly divides the input size
    :param input_size: Size of one side
    :return: board size
    """
    standard_size = 512
    return (standard_size // input_size) * input_size


def get_intervals(board_size, input_size):
    """
    Get interval size for colour changing
    :param board_size: Size of board in pixels
    :param input_size: Dimension
    :return: Interval size
    """
    return board_size // input_size

