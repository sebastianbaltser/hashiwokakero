from services import SolvePuzzle
from reader import User
from reader import StubbedInput
from output import Console


class TestSolvePuzzle:
    def test_application(self):
        stubbed_input = StubbedInput()
        reader = User(stubbed_input)
        console = Console()
        app = SolvePuzzle(reader, console)
        output = console.track_output()
        app()

        expected = " 1 \n | \n 1 \n"

        assert expected in output
