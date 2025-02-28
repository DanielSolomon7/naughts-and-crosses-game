def check_if_draw(given_board):
    finish = True
    for row in given_board:
        for cell in row:
            if cell == []:
                finish = False
    return finish
