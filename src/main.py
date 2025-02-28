from src.get_board import get_board
from src.check_board_format import check_board_format
from src.check_if_naught_or_cross import check_if_naught_or_cross
from src.select_player2 import select_player2
from switch_player import switch_player
from src.board_to_print import board_to_print
from src.selection_board import selection_board
from src.check_if_valid_number import check_if_valid_number
from src.have_turn import have_turn
from src.check_if_position_taken import check_if_position_taken
from src.check_if_game_finished import check_if_game_finished
from src.check_if_draw import check_if_draw


def naughts_and_crosses():
    board = get_board()
    if check_board_format(board):
        # Select players
        players_selected = False
        while not players_selected:
            player1 = input("Player 1 - Please choose 'O' or 'X':")
            if not check_if_naught_or_cross(player1):
                print("Incorrect input. Please enter either 'O' or 'X'")
            else:
                player2 = select_player2(player1)
                players_selected = True
                print(f"Player 1 is {player1}, and Player 2 is {player2}.")

        # Start game
        game_finished = False
        game_won = False
        game_draw = False
        player_turn = player2
        while not game_finished:  # or not game_draw:
            player_turn = switch_player(player_turn)

            print(board_to_print(board))
            print(selection_board(board))

            valid_number = False
            while not valid_number:
                # Allow player to choose position on the board
                turn_number = input(
                    f"Player {player_turn} - Select position on the board (1-9):"
                )
                # Check if valid position number is given
                valid_number = check_if_valid_number(turn_number)
                if not valid_number:
                    print("Invalid input given. Please enter an integer from 1-9.")

                # Check if board position is already taken
                else:
                    valid_number = not check_if_position_taken(int(turn_number), board)
                    if not valid_number:
                        print("Position number already taken. Please try again.")

            # Place player input on the board
            board = have_turn(player_turn, int(turn_number), board)

            print(board_to_print(board))
            print(f"Player {player_turn} selected postion {turn_number} on the board.")

            # Check if the game is finished
            game_finished = check_if_game_finished(board)
            game_won = game_finished

            # Check if the game is a draw
            if not game_finished:
                game_draw = check_if_draw(board)
                game_finished = game_draw

        # Finish game
        if game_won:
            print(f"Player {player_turn} wins!!!")
        elif game_draw:
            print("Game is a draw!")


naughts_and_crosses()
