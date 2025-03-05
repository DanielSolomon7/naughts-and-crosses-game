from copy import deepcopy


def selection_board(given_board):
    """Returns a selection format of a naughts and crosses
    board as a string, which shows the availble board
    position numbers

    Args:
        given_board: a list of 3 lists (each list with a length of 3)

    Returns:
        string: a selection format of the board
    """
    board_copy = deepcopy(given_board)
    counter = 0
    row_num = 0
    for row in given_board:
        index = 0
        for cell in row:
            counter += 1
            if cell == []:
                board_copy[row_num][index] = str(counter)
            index += 1
        row_num += 1

    board = f"""   
 {board_copy[0][0]} | {board_copy[0][1]} | {board_copy[0][2]} 
-----------
 {board_copy[1][0]} | {board_copy[1][1]} | {board_copy[1][2]} 
-----------
 {board_copy[2][0]} | {board_copy[2][1]} | {board_copy[2][2]} 
"""
    return board
