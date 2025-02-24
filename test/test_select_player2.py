from src.select_player2 import select_player2
import pytest


class TestSelectPlayer:
    def test_function_returns_a_string(self):
        input = "X"
        output = select_player2(input)
        assert isinstance(output, str)

    def test_function_identifies_cross_input(self):
        input = "X"
        expected = "O"
        output = select_player2(input)
        assert output == expected

    def test_function_identifies_naught_input(self):
        input = "O"
        expected = "X"
        output = select_player2(input)
        assert output == expected

    def test_function_handles_invalid_input(self):
        input = "Hello"
        with pytest.raises(TypeError) as e:
            select_player2(input)
        assert str(e.value) == "TypeError: given input must be either 'O' or 'X'."
