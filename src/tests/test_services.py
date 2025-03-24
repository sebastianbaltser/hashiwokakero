from services import SolvePuzzle
from reader import UserInput


class TestSolvePuzzle:
    def test_application(self):
        user_input = UserInput()
        app = SolvePuzzle(user_input)
        result = app()
        expected = (
            " 1 \n"
            " | \n"
            " 1 \n"
        )
        assert result == expected
        