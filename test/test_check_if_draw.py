from src.check_if_draw import check_if_draw


class TestCheckIfDraw:
    def test_function_returns_a_boolean(self):
        input = [["X", "O", "X"], ["X", "O", "X"], ["O", "X", "O"]]
        output = check_if_draw(input)
        assert isinstance(output, bool)

    def test_function_identifies_a_draw(self):
        input = [["X", "O", "X"], ["X", "O", "X"], ["O", "X", "O"]]
        expected = True
        output = check_if_draw(input)
        assert output == expected

    def test_function_identifies_if_game_not_finished(self):
        input = [["X", [], "X"], ["X", "O", "X"], ["O", "X", "O"]]
        expected = False
        output = check_if_draw(input)
        assert output == expected
