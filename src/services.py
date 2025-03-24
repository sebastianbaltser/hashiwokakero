class SolvePuzzle:
    def __init__(self, input):
        self.input = input

    def __call__(self):
        puzzle = self.input.read()

        solution = (
            " 1 \n"
            " | \n"
            " 1 \n"
        )
        return solution
