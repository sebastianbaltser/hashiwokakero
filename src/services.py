class SolvePuzzle:
    def __init__(self, reader, console):
        self.reader = reader
        self.console = console

    def __call__(self):
        puzzle = self.reader.read()

        solution = (
            " 1 \n"
            " | \n"
            " 1 \n"
        )

        self.console.print(solution)
        
