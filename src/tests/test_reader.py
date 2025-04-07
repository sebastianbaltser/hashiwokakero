from reader import User
from reader import StubbedInput


class TestUser:
    def tests_returns_input(self):
        stubbed_input = StubbedInput()
        user = User(stubbed_input)
        result = user.read()
        assert result == [[None, 1, None], [None, None, None], [None, 1, None]]

    def test_converts_strings_to_numbers(self):
        stubbed_input = StubbedInput(input=" 2 \n   \n 2 \n")
        user = User(stubbed_input)
        result = user.read()
        assert result == [[None, 2, None], [None, None, None], [None, 2, None]]
