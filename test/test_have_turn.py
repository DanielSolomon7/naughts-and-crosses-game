from src.have_turn import have_turn
import pytest


class TestHaveTurn:
    def test_function_returns_a_list(self):
        output = have_turn("O", 1, [[[], [], []], [[], [], []], [[], [], []]])
        assert isinstance(output, list)

    def test_function_adds_naught_to_function(self):
        pass
