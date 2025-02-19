def check_if_game_finished(given_board):
    cross = "X"
    naught = "O"

    """Check rows"""
    for i in range(3):
        if (
            given_board[i][0] == cross
            and given_board[i][1] == cross
            and given_board[i][2] == cross
        ):
            return True
        elif (
            given_board[i][0] == naught
            and given_board[i][1] == naught
            and given_board[i][2] == naught
        ):
            return True

    """Check columns"""
    for i in range(3):
        if (
            given_board[0][i] == cross
            and given_board[1][i] == cross
            and given_board[2][i] == cross
        ):
            return True
        elif (
            given_board[0][i] == naught
            and given_board[1][i] == naught
            and given_board[2][i] == naught
        ):
            return True

    """Check diagonal left to right"""
    if (
        given_board[0][0] == cross
        and given_board[1][1] == cross
        and given_board[2][2] == cross
    ):
        return True
    elif (
        given_board[0][0] == naught
        and given_board[1][1] == naught
        and given_board[2][2] == naught
    ):
        return True

    """Check diagonal right to left"""
    if (
        given_board[0][2] == cross
        and given_board[1][1] == cross
        and given_board[2][0] == cross
    ):
        return True
    elif (
        given_board[0][2] == naught
        and given_board[1][1] == naught
        and given_board[2][0] == naught
    ):
        return True

    return False
