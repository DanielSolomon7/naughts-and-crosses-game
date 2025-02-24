def select_player2(player1_input):
    if player1_input == "O":
        return "X"
    elif player1_input == "X":
        return "O"
    else:
        raise TypeError("TypeError: given input must be either 'O' or 'X'.")
