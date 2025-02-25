from src.get_board import get_board
from src.check_board_format import check_board_format
from src.check_if_naught_or_cross import check_if_naught_or_cross
from src.select_player2 import select_player2
from src.board_to_print import board_to_print
from src.selection_board import selection_board
from src.have_turn import have_turn


def naughts_and_crosses():
    board = get_board()
    if check_board_format(board) == True:
        # Select Players
        players_selected = False
        while not players_selected:
            player1 = input("Player 1 - Please choose 'O' or 'X':")
            if not check_if_naught_or_cross(player1):
                print("Incorrect input. Please enter either 'O' or 'X'")
            else:
                player2 = select_player2(player1)
                players_selected = True
                print(f"Player 1 is {player1}, and Player 2 is {player2}.")

        # Start Game
        game_finished = False
        player_turn = player2
        while not game_finished:
            if player_turn == player1:
                player_turn = player2
            else:
                player_turn = player1

            print(board_to_print(board))
            print(selection_board(board))
            turn_number = int(input(f"Player {player_turn} - Select position on the board (1-9):"))
            board = have_turn(player_turn, turn_number, board)
            print(board_to_print(board))
            print(f"Player {player_turn} selected postion {turn_number} on the board.")

            game_finished = True


naughts_and_crosses()
