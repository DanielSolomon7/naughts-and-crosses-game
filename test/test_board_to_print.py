from src.board_to_print import board_to_print


class TestBoardToPrint:
    def test_function_returns_a_string(self):
        input = [[[], [], []], [[], [], []], [[], [], []]]
        output = board_to_print(input)
        assert isinstance(output, str)

    def test_function_returns_empty_board_as_str_in_displaying_format(self):
        input = [[[], [], []], [[], [], []], [[], [], []]]
        expected = """   
   |   |   
-----------
   |   |   
-----------
   |   |   
"""
        output = board_to_print(input)
        assert output == expected

    def test_function_returns_filled_board_as_str_in_displaying_format(self):
        input = [["X", "O", "X"], ["O", "O", "X"], ["X", "X", "O"]]
        expected = """   
 X | O | X 
-----------
 O | O | X 
-----------
 X | X | O 
"""
        output = board_to_print(input)
        assert output == expected

    def test_function_returns_partly_filled_board_as_str_in_displaying_format(self):
        input = [["X", [], "X"], [[], "O", []], ["X", "O", []]]
        expected = """   
 X |   | X 
-----------
   | O |   
-----------
 X | O |   
"""
        output = board_to_print(input)
        assert output == expected
