def check_if_position_taken(position_num, given_board):
    """Checks if a board postion has already been taken

    Args:
        postion_num (int): a position number for the board (should be from 1-9)
        given_board (list): a list of 3 lists (each list with a length of 3)

    Returns:
        boolean: returns True if position is taken,
                 returns False if position is not taken
    """
    if not isinstance(position_num, int):
        raise TypeError("TypeError: given postion number must be an integer from 1-9.")
    if position_num < 1 or position_num > 9:
        raise ValueError(
            "ValueError: given postion number must be an integer from 1-9."
        )

    if position_num > 0 and position_num < 4:
        row_number = 0
        column_num = position_num - 1
    elif position_num > 3 and position_num < 7:
        row_number = 1
        column_num = position_num - 4
    elif position_num > 6 and position_num < 10:
        row_number = 2
        column_num = position_num - 7

    if given_board[row_number][column_num] == []:
        return False
    else:
        return True
