from src.select_player import select_player
import pytest


class TestSelectPlayer:
    def test_function_returns_a_dict(self):
        input = "X"
        output = select_player(input)
        assert isinstance(output, dict)

    def test_function_identifies_cross_input(self):
        input = "X"
        expected = {"Player 1": "X", "Player 2": "O"}
        output = select_player(input)
        assert output == expected

    def test_function_identifies_naught_input(self):
        input = "O"
        expected = {"Player 1": "O", "Player 2": "X"}
        output = select_player(input)
        assert output == expected

    def test_function_handles_invalid_input(self):
        input = "Hello"
        with pytest.raises(TypeError) as e:
            select_player(input)
        assert str(e.value) == "TypeError: given input must be either 'O' or 'X'."
