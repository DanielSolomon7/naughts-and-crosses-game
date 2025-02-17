from src.have_turn import have_turn
import pytest


class TestHaveTurn:
    def test_function_returns_a_list(self):
        output = have_turn("O", 1, [[[], [], []], [[], [], []], [[], [], []]])
        assert isinstance(output, list)

    def test_function_adds_naught_to_board_at_correct_position(self):
        input_turn = "X"
        input_number = 3
        input_board = [[[], [], []], [[], [], []], [[], [], []]]
        expected = [[[], [], "X"], [[], [], []], [[], [], []]]
        output = have_turn(input_turn, input_number, input_board)
        assert output == expected

        input_turn = "X"
        input_number = 5
        input_board = [[[], [], []], [[], [], []], [[], [], []]]
        expected = [[[], [], []], [[], "X", []], [[], [], []]]
        output = have_turn(input_turn, input_number, input_board)
        assert output == expected

        input_turn = "X"
        input_number = 9
        input_board = [[[], [], []], [[], [], []], [[], [], []]]
        expected = [[[], [], []], [[], [], []], [[], [], "X"]]
        output = have_turn(input_turn, input_number, input_board)
        assert output == expected

    def test_function_adds_cross_to_board_at_correct_position(self):
        input_turn = "O"
        input_number = 8
        input_board = [[[], [], []], [[], [], []], [[], [], []]]
        expected = [[[], [], []], [[], [], []], [[], "O", []]]
        output = have_turn(input_turn, input_number, input_board)
        assert output == expected

        input_turn = "O"
        input_number = 1
        input_board = [[[], [], []], [[], [], []], [[], [], []]]
        expected = [["O", [], []], [[], [], []], [[], [], []]]
        output = have_turn(input_turn, input_number, input_board)
        assert output == expected

        input_turn = "O"
        input_number = 6
        input_board = [[[], [], []], [[], [], []], [[], [], []]]
        expected = [[[], [], []], [[], [], "O"], [[], [], []]]
        output = have_turn(input_turn, input_number, input_board)
        assert output == expected

    def test_function_handles_invalid_turn_parameter(self):
        input_turn = 5
        input_number = 6
        input_board = [[[], [], []], [[], [], []], [[], [], []]]
        with pytest.raises(ValueError) as e:
            have_turn(input_turn, input_number, input_board)
        assert str(e.value) == "ValueError: given turn must be either 'X' or 'O'"

    def test_function_handles_invalid_position_number_type(self):
        input_turn = "O"
        input_number = "Hi"
        input_board = [[[], [], []], [[], [], []], [[], [], []]]
        with pytest.raises(TypeError) as e:
            have_turn(input_turn, input_number, input_board)
        assert (
            str(e.value)
            == "TypeError: given postion number must be an integer from 1-9."
        )

    def test_function_handles_out_of_range_position_number(self):
        input_turn = "O"
        input_number = 0
        input_board = [[[], [], []], [[], [], []], [[], [], []]]
        with pytest.raises(ValueError) as e:
            have_turn(input_turn, input_number, input_board)
        assert (
            str(e.value)
            == "ValueError: given postion number must be an integer from 1-9."
        )

        input_turn = "O"
        input_number = 10
        input_board = [[[], [], []], [[], [], []], [[], [], []]]
        with pytest.raises(ValueError) as e:
            have_turn(input_turn, input_number, input_board)
        assert (
            str(e.value)
            == "ValueError: given postion number must be an integer from 1-9."
        )
