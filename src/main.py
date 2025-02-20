from src.get_board import get_board
from src.check_board_format import check_board_format


def naughts_and_crosses():
    board = get_board()
    if check_board_format(board) == True:
        player1 = input("Player 1 - Please choose 'O' or 'X':")
        
