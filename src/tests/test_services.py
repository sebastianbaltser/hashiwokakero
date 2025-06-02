import pytest
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

    @pytest.mark.parametrize("x", [0, 1, 2])
    def test_horizontally_shifted_islands(self, x):
        islands = {Island(x, 0, 1), Island(x, 2, 1)}
        stubbed_input = StubbedInput(islands)
        reader = User(stubbed_input)
        console = Console()
        app = SolvePuzzle(reader, console)
        output = console.track_output()
        app()

        lines = output[0].splitlines()
        assert lines[0][x] == "1"
        assert lines[1][x] == "|"
        assert lines[2][x] == "1"
