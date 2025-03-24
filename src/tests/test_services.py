from services import SolvePuzzle
from reader import User


class TestSolvePuzzle:
    def test_application(self):
        reader = User()
        app = SolvePuzzle(reader)
        result = app()
        expected = (
            " 1 \n"
            " | \n"
            " 1 \n"
        )
        assert result == expected
