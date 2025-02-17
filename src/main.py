from src.get_board import get_board
from src.check_board_format import check_board_format


def naughts_and_crosses():
    board = get_board()
    check_board_format(board)
