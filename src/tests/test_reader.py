import pytest

from reader import User
from reader import StubbedInput
from model import Island


class TestUser:
    def tests_returns_input(self):
        stubbed_input = StubbedInput()
        user = User(stubbed_input)
        result = user.read()
        assert result == [Island(1, 2, 1), Island(1, 0, 1)]

    @pytest.mark.parametrize("number", [2, 3, 4, 5, 6, 7, 8])
    def test_converts_strings_to_numbers(self, number):
        stubbed_input = StubbedInput(response=f" {number} \n   \n {number} \n")
        user = User(stubbed_input)
        result = user.read()
        assert result == [Island(1, 2, number), Island(1, 0, number)]
