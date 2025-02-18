from src.board_to_print import board_to_print


class TestBoardToPrint:
    def test_function_returns_a_string(self):
        input = [[[], [], []], [[], [], []], [[], [], []]]
        output = board_to_print(input)
        assert isinstance(output, str)

    def test_function_returns_empty_board_as_str_in_displaying_format(self):
        input = [[[], [], []], [[], [], []], [[], [], []]]
        expected = """   
   |  |  
----------
   |  |  
----------
   |  |   
"""
        output = board_to_print(input)
        assert output == expected
