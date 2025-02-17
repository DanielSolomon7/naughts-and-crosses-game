def check_if_position_taken(position_num, given_board):
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
