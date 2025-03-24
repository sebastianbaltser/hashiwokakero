from services import SolvePuzzle
from reader import User
from reader import StubbedInput


class TestSolvePuzzle:
    def test_application(self):
        stubbed_input = StubbedInput()
        reader = User(stubbed_input)
        app = SolvePuzzle(reader)
        result = app()
        expected = (
            " 1 \n"
            " | \n"
            " 1 \n"
        )
        assert result == expected
