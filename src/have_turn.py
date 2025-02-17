def have_turn(turn, position_number, given_board):
    if turn != "X" and turn != "O":
        raise ValueError("ValueError: given turn must be either 'X' or 'O'")
    if not isinstance(position_number, int):
        raise TypeError("TypeError: given postion number must be an integer from 1-9.")
    if position_number < 1 or position_number > 9:
        raise ValueError(
            "ValueError: given postion number must be an integer from 1-9."
        )

    if position_number > 0 and position_number < 4:
        given_board[0][position_number - 1] = turn
    elif position_number > 3 and position_number < 7:
        given_board[1][position_number - 4] = turn
    elif position_number > 6 and position_number < 10:
        given_board[2][position_number - 7] = turn
    return given_board
