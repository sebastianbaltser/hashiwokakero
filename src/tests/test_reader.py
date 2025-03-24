from reader import UserInput

class TestUserInput:
    def tests_returns_input(self):
        user_input = UserInput()
        result = user_input.read()
        assert result == (
            " 1 \n"
            "   \n"
            " 1 \n"
        )