def check_if_draw(given_board):
    """Checks if a naughts and crosses game is finished
    as a draw

    Args:
        given_board: a list of 3 lists (each list with a length of 3)

    Returns:
        boolean: returns True if finished as a draw,
                 returns False if not finished as a draw
    """
    finish = True
    for row in given_board:
        for cell in row:
            if cell == []:
                finish = False
                break
    return finish
