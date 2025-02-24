from src.get_board import get_board
from src.check_board_format import check_board_format
from src.check_if_naught_or_cross import check_if_naught_or_cross
from src.select_player2 import select_player2


def naughts_and_crosses():
    board = get_board()
    if check_board_format(board) == True:
        players_selected = False
        while players_selected == False:
            player1 = input("Player 1 - Please choose 'O' or 'X':")
            if not check_if_naught_or_cross(player1):
                print("Incorrect input. Please enter either 'O' or 'X'")
            else:
                player2 = select_player2(player1)
                players_selected = True
                print(f"Player 1 is {player1}, and Player 2 is {player2}.")


naughts_and_crosses()
