def check_board_format(given_board):
    if not isinstance(given_board, list):
        raise TypeError("TypeError: given board must be a list.")
    if len(given_board) != 3:
        raise ValueError("ValueError: given board must be a list of 3 lists.")
    for row in given_board:
        if not isinstance(row, list):
            raise ValueError("ValueError: given board must be a list of 3 lists.")
        if len(row) != 3:
            raise ValueError(
                "ValueError: given board must be a list of 3 lists, with all 3 lists containing 3 items."
            )
        for item in row:
            if item != [] or item != "X" or item != "O":
                raise ValueError(
                    "ValueError: given board must be a list of 3 lists, with all 3 lists containing 3 items (which must contain either: a list, 'X', or 'O')."
                )
