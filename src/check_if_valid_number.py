def check_if_valid_number(given_num):
    """Checks if a given number is a valid board position on
    a naughts and crosses board

    Args:
        given_num: a given input

    Returns:
        boolean: returns True if a valid number,
                 returns False if not a valid number
    """
    if given_num in [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ]:
        return True
    return False
