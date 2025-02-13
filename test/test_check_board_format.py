from src.check_board_format import check_board_format
import pytest


class TestCheckBoardFormat:
    def test_function_handles_non_list_type_given(self):
        input = 5
        with pytest.raises(TypeError) as e:
            check_board_format(input)
        assert str(e.value) == "TypeError: given board must be a list."

    def test_function_handles_list_with_incorrect_board_size(self):
        input = [[[], [], []], [[], [], []]]
        with pytest.raises(ValueError) as e:
            check_board_format(input)
        assert str(e.value) == "ValueError: given board must be a list of 3 lists."

    def test_function_handles_list_without_3_lists(self):
        input = [[[], [], []], [[], [], []], 5]
        with pytest.raises(ValueError) as e:
            check_board_format(input)
        assert str(e.value) == "ValueError: given board must be a list of 3 lists."

    def test_function_handles_row_without_3_lists(self):
        input = [[[], [], []], [[], [], []], [[], []]]
        with pytest.raises(ValueError) as e:
            check_board_format(input)
        assert (
            str(e.value)
            == "ValueError: given board must be a list of 3 lists, with all 3 lists containing 3 items (which must contain either: a list, 'X', or 'O')."
        )

    def test_function_handles_row_without_list_or_X_or_O(self):
        input = [[[], "X", "O"], ["O", [], "X"], ["O", "X", 5]]
        with pytest.raises(ValueError) as e:
            check_board_format(input)
        assert (
            str(e.value)
            == "ValueError: given board must be a list of 3 lists, with all 3 lists containing 3 items (which must contain either: a list, 'X', or 'O')."
        )

    def test_function_identifies_correct_board(self):
        input = [[[], "X", "O"], ["O", "X", []], ["O", [], "X"]]
        output = check_board_format(input)
        assert output == True
