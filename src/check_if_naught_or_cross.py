def check_if_naught_or_cross(input):
    """Checks if the given input is a valid naught or cross

    Args:
        input: a given input

    Returns:
        boolean: returns True if a valid naught or cross,
                 returns False if not a valid naught or cross
    """
    if input == "O" or input == "X":
        return True
    return False
