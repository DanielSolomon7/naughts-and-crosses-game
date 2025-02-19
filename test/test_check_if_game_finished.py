from src.check_if_game_finished import check_if_game_finished


class TestCheckIfGameFinished:
    def test_function_returns_a_boolean(self):
        input = [[[], [], []], [[], [], []], [[], [], []]]
        output = check_if_game_finished(input)
        assert isinstance(output, bool)

    def test_function_indentifies_empty_board(self):
        input = [[[], [], []], [[], [], []], [[], [], []]]
        output = check_if_game_finished(input)
        assert output == False

    def test_function_indentifies_unfinished_empty_game(self):
        input = [[[], [], []], [[], [], []], [[], [], []]]
        output = check_if_game_finished(input)
        assert output == False

    def test_function_indentifies_unfinished_but_not_empty_game(self):
        input = [["O", [], "X"], ["X", "O", []], [[], "O", "X"]]
        output = check_if_game_finished(input)
        assert output == False

        input = [["X", "X", []], [[], "O", "O"], ["X", [], "O"]]
        output = check_if_game_finished(input)
        assert output == False

    def test_function_indentifies_finished_game_from_top_row(self):
        input = [["X", "X", "X"], ["O", "O", []], [[], [], []]]
        output = check_if_game_finished(input)
        assert output == True

    def test_function_indentifies_finished_game_from_middle_row(self):
        input = [["X", [], "X"], ["O", "O", "O"], [[], [], []]]
        output = check_if_game_finished(input)
        assert output == True

    def test_function_indentifies_finished_game_from_bottom_row(self):
        input = [[[], [], []], ["O", [], "O"], ["X", "X", "X"]]
        output = check_if_game_finished(input)
        assert output == True

    def test_function_indentifies_finished_game_from_left_column(self):
        input = [["O", [], []], ["O", [], "X"], ["O", "X", "X"]]
        output = check_if_game_finished(input)
        assert output == True

    def test_function_indentifies_finished_game_from_middle_column(self):
        input = [["O", "X", []], [[], "X", "X"], ["O", "X", "O"]]
        output = check_if_game_finished(input)
        assert output == True

    def test_function_indentifies_finished_game_from_right_column(self):
        input = [["O", "X", "O"], [[], [], "O"], ["X", "X", "O"]]
        output = check_if_game_finished(input)
        assert output == True

    def test_function_indentifies_finished_game_from_diagonal_left_to_right(self):
        input = [["O", "X", "O"], [[], "O", []], ["X", "X", "O"]]
        output = check_if_game_finished(input)
        assert output == True

    def test_function_indentifies_finished_game_from_diagonal_right_to_left(self):
        input = [["O", [], "X"], [[], "X", []], ["X", "O", "O"]]
        output = check_if_game_finished(input)
        assert output == True
