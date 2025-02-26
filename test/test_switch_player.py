from src.switch_player import switch_player
import pytest


class TestSwitchPlayer:
    def test_function_returns_a_string(self):
        input = "X"
        output = switch_player(input)
        assert isinstance(output, str)

    def test_function_identifies_cross_input(self):
        input = "X"
        expected = "O"
        output = switch_player(input)
        assert output == expected

    def test_function_identifies_naught_input(self):
        input = "O"
        expected = "X"
        output = switch_player(input)
        assert output == expected

    def test_function_handles_invalid_input(self):
        input = "Hello"
        with pytest.raises(TypeError) as e:
            switch_player(input)
        assert str(e.value) == "TypeError: given input must be either 'O' or 'X'."
