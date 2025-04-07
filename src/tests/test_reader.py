import pytest

from reader import User
from reader import StubbedInput


class TestUser:
    def tests_returns_input(self):
        stubbed_input = StubbedInput()
        user = User(stubbed_input)
        result = user.read()
        assert result == [[None, 1, None], [None, None, None], [None, 1, None]]

    @pytest.mark.parametrize("number", [2, 3, 4, 5, 6, 7, 8])
    def test_converts_strings_to_numbers(self, number):
        stubbed_input = StubbedInput(response=f" {number} \n   \n {number} \n")
        user = User(stubbed_input)
        result = user.read()
        assert result == [
            [None, number, None],
            [None, None, None],
            [None, number, None],
        ]

    def test_converts_space_character_to_none(self):
        stubbed_input = StubbedInput(response="   \n   \n 1 \n")
        user = User(stubbed_input)
        result = user.read()
        assert result[0][1] is None
        assert result[2][1] == 1

    def test_places_numbers_in_correct_positions(self):
        stubbed_input = StubbedInput(response="1  \n   \n   \n")
        user = User(stubbed_input)
        result = user.read()
        assert result[0][0] == 1
