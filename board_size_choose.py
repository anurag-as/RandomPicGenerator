def choose_board_size(input_size):
    """
    Choose a board size based on input size, which evenly divides the input size
    :param input_size: Size of one side
    :return: board size
    """
    standard_size = 1024
    return (standard_size // input_size) * input_size

