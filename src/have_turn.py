def have_turn(turn, number, given_board):
    if turn != "X" and turn != "O":
        raise ValueError("ValueError: given turn must be either 'X' or 'O'")
    if not isinstance(number, int):
        raise TypeError("TypeError: given postion number must be an integer from 1-9.")
    if number < 1 or number > 9:
        raise ValueError(
            "ValueError: given postion number must be an integer from 1-9."
        )

    if number > 0 and number < 4:
        given_board[0][number - 1] = turn
    elif number > 3 and number < 7:
        given_board[1][number - 4] = turn
    elif number > 6 and number < 10:
        given_board[2][number - 7] = turn
    return given_board
