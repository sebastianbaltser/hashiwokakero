import pytest

from reader import User
from reader import StubbedInput


class TestUser:
    def tests_returns_input(self):
        stubbed_input = StubbedInput()
        user = User(stubbed_input)
        result = user.read()
        assert result == [[None, 1, None], [None, None, None], [None, 1, None]]

    @pytest.mark.parametrize('number', [2, 3])
    def test_converts_strings_to_numbers(self, number):
        stubbed_input = StubbedInput(response=f" {number} \n   \n {number} \n")
        user = User(stubbed_input)
        result = user.read()
        assert result == [[None, number, None], [None, None, None], [None, number, None]]
