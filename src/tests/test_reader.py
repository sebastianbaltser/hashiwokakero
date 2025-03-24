from reader import User

class TestUser:
    def tests_returns_input(self):
        user = User()
        result = user.read()
        assert result == (
            " 1 \n"
            "   \n"
            " 1 \n"
        )