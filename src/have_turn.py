def have_turn(turn, number, given_board):
    if number > 0 and number < 4:
        given_board[0][number - 1] = turn
    elif number > 3 and number < 7:
        given_board[1][number - 4] = turn
    elif number > 6 and number < 10:
        given_board[2][number - 7] = turn
    return given_board
