from reader import User
from reader import StubbedInput


class TestUser:
    def tests_returns_input(self):
        stubbed_input = StubbedInput()
        user = User(stubbed_input)
        result = user.read()
        assert result == (" 1 \n   \n 1 \n")
