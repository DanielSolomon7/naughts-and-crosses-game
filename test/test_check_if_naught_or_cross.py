from src.check_if_naught_or_cross import check_if_naught_or_cross


class TestCheckIfNaughtOrCross:
    def test_function_returns_a_boolean(self):
        input = "X"
        output = check_if_naught_or_cross(input)
        assert isinstance(output, bool)

    def test_function_identifies_a_cross(self):
        input = "X"
        output = check_if_naught_or_cross(input)
        assert output == True

    def test_function_identifies_a_naught(self):
        input = "O"
        output = check_if_naught_or_cross(input)
        assert output == True

    def test_function_identifies_if_input_is_not_a_naught_or_cross(self):
        input = "5"
        output = check_if_naught_or_cross(input)
        assert output == False

        input = 10
        output = check_if_naught_or_cross(input)
        assert output == False
