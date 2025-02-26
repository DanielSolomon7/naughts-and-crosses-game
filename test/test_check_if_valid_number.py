from src.check_if_valid_number import check_if_valid_number


class TestCheckIfValidNumber:
    def test_function_returns_a_boolean(self):
        input = 5
        output = check_if_valid_number(input)
        assert isinstance(output, bool)

    def test_function_identifies_valid_number(self):
        input = 5
        expected = True
        output = check_if_valid_number(input)
        assert output == expected

    def test_function_identifies_too_low_number(self):
        input = 0
        expected = False
        output = check_if_valid_number(input)
        assert output == expected

    def test_function_identifies_too_high_number(self):
        input = 10
        expected = False
        output = check_if_valid_number(input)
        assert output == expected

    def test_function_identifies_invalid_type_given(self):
        input = "Hi"
        expected = False
        output = check_if_valid_number(input)
        assert output == expected
