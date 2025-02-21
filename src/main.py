from src.get_board import get_board
from src.check_board_format import check_board_format
from src.check_if_naught_or_cross import check_if_naught_or_cross


def naughts_and_crosses():
    board = get_board()
    if check_board_format(board) == True:
        player1 = input("Player 1 - Please choose 'O' or 'X':")
        if not check_if_naught_or_cross(player1):
            print("Incorrect input. Please enter either 'O' or 'X'")
        else:
            if player1 == "O":
                player2 = "X"
            else:
                player2 == "O"
