def switch_player(player):
    """Switches player, from "O" to "X", or "X" to "O"

    Args:
        player: given input, which should be a string of "O" or "X"

    Returns:
        string: a string of the next player, either "O" or "X"
    """
    if player == "O":
        return "X"
    elif player == "X":
        return "O"
    else:
        raise TypeError("TypeError: given input must be either 'O' or 'X'.")
