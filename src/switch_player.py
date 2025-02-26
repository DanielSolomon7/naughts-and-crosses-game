def switch_player(player):
    if player == "O":
        return "X"
    elif player == "X":
        return "O"
    else:
        raise TypeError("TypeError: given input must be either 'O' or 'X'.")
