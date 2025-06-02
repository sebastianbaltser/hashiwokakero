class SolvePuzzle:
    def __init__(self, reader, console):
        self.reader = reader
        self.console = console

    def __call__(self):
        puzzle = self.reader.read()
        board = "   \n   \n   \n"

        for island in puzzle:
            x = island.x

            board = board[:x] + "1" + board[x + 1 :]
            board = board[: x + 4] + "|" + board[x + 1 + 4 :]
            board = board[: x + 8] + "1" + board[x + 1 + 8 :]

        solution = board
        self.console.print(solution)
