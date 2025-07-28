import pytest
from services import SolvePuzzle
from reader import User
from reader import StubbedInput
from output import Console
from model import Island


class TestSolvePuzzle:
    def run_app(self, islands):
        stubbed_input = StubbedInput(islands)
        reader = User(stubbed_input)
        console = Console()
        app = SolvePuzzle(reader, console)
        output = console.track_output()
        app()
        return output

    def test_application(self):
        islands = {Island(1, 2, 1), Island(1, 0, 1)}
        output = self.run_app(islands)

        expected = " 1 \n | \n 1 \n"

        assert expected in output

    @pytest.mark.parametrize("x", [0, 1, 2])
    def test_horizontally_shifted_islands(self, x):
        islands = {Island(x, 0, 1), Island(x, 2, 1)}
        output = self.run_app(islands)

        lines = output[0].splitlines()
        assert lines[0][x] == "1"
        assert lines[1][x] == "|"
        assert lines[2][x] == "1"

    def test_multiple_vertical_bridges(self):
        islands = {
            Island(0, 0, 1),
            Island(0, 2, 1),
            Island(1, 2, 1),
            Island(1, 0, 1),
            Island(2, 0, 1),
            Island(2, 2, 1),
        }
        output = self.run_app(islands)

        expected = "111\n|||\n111\n"

        assert expected in output

    @pytest.mark.parametrize("y", [0, 1, 2])
    def test_horizontal_bridge(self, y):
        islands = {Island(0, y, 1), Island(2, y, 1)}
        output = self.run_app(islands)

        lines = list(reversed(output[0].splitlines()))
        assert lines[y] == "1-1"
        assert len(lines) == 3

    @pytest.mark.parametrize(
        "islands, expected",
        [
            ({Island(2, 2, 1), Island(0, 2, 2), Island(0, 0, 1)}, "2-1\n|  \n1  \n"),
            ({Island(2, 0, 1), Island(2, 2, 2), Island(0, 2, 1)}, "1-2\n  |\n  1\n"),
            ({Island(2, 0, 1), Island(0, 0, 2), Island(0, 2, 1)}, "1  \n|  \n2-1\n"),
            ({Island(2, 2, 1), Island(2, 0, 2), Island(0, 0, 1)}, "  1\n  |\n1-2\n"),
            (
                {Island(2, 2, 2), Island(2, 0, 2), Island(0, 0, 2), Island(0, 2, 2)},
                "2-2\n| |\n2-2\n",
            ),
        ],
    )
    def test_island_with_two_bridges(self, islands, expected):
        output = self.run_app(islands)

        assert expected in output
