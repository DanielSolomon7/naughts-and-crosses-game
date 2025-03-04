def select_player2(player1_input):
    """Identifies if player 1 is a naught or cross, and returns
    what player 2 will be

    Args:
        player1_input: given input, which should be a string of "O" or "X"

    Returns:
        string: a string of player 2, either "O" or "X"
    """
    if player1_input == "O":
        return "X"
    elif player1_input == "X":
        return "O"
    else:
        raise TypeError("TypeError: given input must be either 'O' or 'X'.")
