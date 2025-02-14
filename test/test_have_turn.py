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

    def test_function_adds_cross_to_board_at_correct_position(self):
        input_turn = "O"
        input_number = 8
        input_board = [[[], [], []], [[], [], []], [[], [], []]]
        expected = [[[], [], []], [[], [], []], [[], "O", []]]
        output = have_turn(input_turn, input_number, input_board)
        assert output == expected
