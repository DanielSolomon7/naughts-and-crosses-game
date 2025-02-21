def select_player(player1_input):
    if player1_input == "O":
        player2 = "X"
    elif player1_input == "X":
        player2 = "O"
    else:
        raise TypeError("TypeError: given input must be either 'O' or 'X'.")

    return {"Player 1": player1_input, "Player 2": player2}
