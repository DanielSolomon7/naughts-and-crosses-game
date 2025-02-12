from src.get_board import get_board


class TestGetBoard:
    def test_function_returns_lists_for_the_board(self):
        output = get_board()
        assert output == [[[], [], []], [[], [], []], [[], [], []]]
