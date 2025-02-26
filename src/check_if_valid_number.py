def check_if_valid_number(given_num):
    if not isinstance(given_num, int):
        return False
    if given_num < 1 or given_num > 9:
        return False
    return True
