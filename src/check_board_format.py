def check_board_format(given_board):
    """Checks if a naughts and crosses board is a
    valid fomat

    Args:
        given_board: a list of 3 lists (each list with a length of 3)

    Returns:
        boolean: returns True if a valid format
    """
    if not isinstance(given_board, list):
        raise TypeError("TypeError: given board must be a list.")
    if len(given_board) != 3:
        raise ValueError("ValueError: given board must be a list of 3 lists.")
    for row in given_board:
        if not isinstance(row, list):
            raise ValueError("ValueError: given board must be a list of 3 lists.")
        if len(row) != 3:
            raise ValueError(
                "ValueError: given board must be a list of 3 lists, with all 3 lists containing 3 items (which must contain either: a list, 'X', or 'O')."
            )
        for item in row:
            if item == [] or item == "X" or item == "O":
                pass
            else:
                print(item)
                raise ValueError(
                    "ValueError: given board must be a list of 3 lists, with all 3 lists containing 3 items (which must contain either: a list, 'X', or 'O')."
                )
    return True
