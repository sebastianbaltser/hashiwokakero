class SolvePuzzle:
    def __init__(self, reader, console):
        self.reader = reader
        self.console = console

    def __call__(self):
        puzzle = self.reader.read()
        board = "   \n   \n   \n"

        for island in puzzle:
            x = island.x

            other_islands = puzzle.copy()
            other_islands.remove(island)

            if any(other_island.x == island.x for other_island in other_islands):
                board = board[:x] + "1" + board[x + 1 :]
                board = board[: x + 4] + "|" + board[x + 1 + 4 :]
                board = board[: x + 8] + "1" + board[x + 1 + 8 :]
            else:
                line_index = 8 - 4 * island.y
                board = board[:line_index] + "1-1" + board[line_index + 3 :]

        solution = board
        self.console.print(solution)
