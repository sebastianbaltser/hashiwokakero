from services import SolvePuzzle


class TestSolvePuzzle:
    def test_application(self):
        app = SolvePuzzle()
        result = app()
        expected = (
            " 1 \n"
            " | \n"
            " 1 \n"
        )
        assert result == expected
