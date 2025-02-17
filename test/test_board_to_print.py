from src.board_to_print import board_to_print


class TestBoardToPrint:
    def test_function_returns_a_string(self):
        input = [[[], [], []], [[], [], []], [[], [], []]]
        output = board_to_print(input)
        assert isinstance(output, str)
