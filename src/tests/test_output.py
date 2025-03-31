from output import Console


class TestConsole:
    def test_tracks_output(self):
        console = Console()
        output = console.track_output()
        console.print("et eller andet")

        assert "et eller andet" in output
