from src.check_if_position_taken import check_if_position_taken
import pytest


class TestCheckIfPositionTaken:
    def test_function_returns_a_boolean(self):
        input_num = 1
        input_board = [[[], [], []], [[], [], []], [[], []]]
        output = check_if_position_taken(input_num, input_board)
        assert isinstance(output, bool)

    def test_function_identifies_empty_board(self):
        input_num = 1
        input_board = [[[], [], []], [[], [], []], [[], []]]
        output = check_if_position_taken(input_num, input_board)
        assert output == False

    def test_function_identifies_position_not_taken(self):
        input_num = 1
        input_board = [[[], "X", []], [[], [], []], [[], []]]
        output = check_if_position_taken(input_num, input_board)
        assert output == False

    def test_function_identifies_position_taken(self):
        input_num = 1
        input_board = [["O", [], []], [[], [], []], [[], []]]
        output = check_if_position_taken(input_num, input_board)
        assert output == True

        input_num = 5
        input_board = [[[], [], []], [[], "X", []], [[], []]]
        output = check_if_position_taken(input_num, input_board)
        assert output == True

        input_num = 9
        input_board = [[[], [], []], [[], [], []], [[], [], "O"]]
        output = check_if_position_taken(input_num, input_board)
        assert output == True

    def test_function_handles_invalid_position_number_type(self):
        input_num = "Hi"
        input_board = [["O", [], []], [[], [], []], [[], []]]
        with pytest.raises(TypeError) as e:
            check_if_position_taken(input_num, input_board)
        assert (
            str(e.value)
            == "TypeError: given postion number must be an integer from 1-9."
        )

    def test_function_handles_out_of_range_position_number(self):
        input_num = 0
        input_board = [["O", [], []], [[], [], []], [[], []]]
        with pytest.raises(ValueError) as e:
            check_if_position_taken(input_num, input_board)
        assert (
            str(e.value)
            == "ValueError: given postion number must be an integer from 1-9."
        )

        input_num = 10
        input_board = [["O", [], []], [[], [], []], [[], []]]
        with pytest.raises(ValueError) as e:
            check_if_position_taken(input_num, input_board)
        assert (
            str(e.value)
            == "ValueError: given postion number must be an integer from 1-9."
        )
