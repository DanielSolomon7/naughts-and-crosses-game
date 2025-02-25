from src.selection_board import selection_board


class TestSelectionBoard:
    def test_function_returns_a_string(self):
        input = [[[], [], []], [[], [], []], [[], [], []]]
        output = selection_board(input)
        assert isinstance(output, str)

    def test_function_identifies_empty_board_and_returns_str_in_selection_format(self):
        input = [[[], [], []], [[], [], []], [[], [], []]]
        expected = """   
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 
"""
        output = selection_board(input)
        assert output == expected

    def test_function_identifies_filled_board(self):
        input = [["X", "O", "X"], ["O", "O", "X"], ["X", "X", "O"]]
        expected = """   
 X | O | X 
-----------
 O | O | X 
-----------
 X | X | O 
"""
        output = selection_board(input)
        assert output == expected

    def test_function_identifies_partly_filled_board_and_returns_str_in_selection_format(
        self,
    ):
        input = [["X", [], "X"], [[], "O", []], ["X", "O", []]]
        expected = """   
 X | 2 | X 
-----------
 4 | O | 6 
-----------
 X | O | 9 
"""
        output = selection_board(input)
        assert output == expected
