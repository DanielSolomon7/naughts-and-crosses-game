from src.have_turn import have_turn
import pytest


class TestHaveTurn:
    def test_function_returns_a_list(self):
        output = have_turn([[[], [], []], [[], [], []], [[], [], []]])
        assert isinstance(output, list)
