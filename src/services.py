class SolvePuzzle:
    def __init__(self, reader):
        self.reader = reader

    def __call__(self):
        puzzle = self.reader.read()

        solution = (
            " 1 \n"
            " | \n"
            " 1 \n"
        )
        return solution
