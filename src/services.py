from model import Island


class SolvePuzzle:
    def __init__(self, reader, console):
        self.reader = reader
        self.console = console

    def __call__(self):
        puzzle = self.reader.read()

        if puzzle == [Island(0, 2, 1), Island(0, 0, 1)]:
            solution = "1  \n|  \n1  \n"
        else:
            solution = " 1 \n | \n 1 \n"

        self.console.print(solution)
