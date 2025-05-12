from services import SolvePuzzle
from reader import User
from reader import StubbedInput
from output import Console
from model import Island


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

    def test_horizontally_shifted_islands(self):
        islands = {Island(0, 0, 1), Island(0, 2, 1)}
        stubbed_input = StubbedInput(islands)
        reader = User(stubbed_input)
        console = Console()
        app = SolvePuzzle(reader, console)
        output = console.track_output()
        app()

        expected = "1  \n|  \n1  \n"

        assert expected in output
