from model import Board


class SolvePuzzle:
    def __init__(self, reader, console):
        self.reader = reader
        self.console = console

    def __call__(self):
        puzzle = self.reader.read()

        self.board = Board()

        pairs = self.solve(puzzle)

        for pair in pairs:
            self.board.draw(pair)

        solution = str(self.board)
        self.console.print(solution)

    def solve(self, puzzle):
        pairs = []
        for island in puzzle:
            other_islands = puzzle.copy()
            other_islands.remove(island)

            if any(other_island.x == island.x for other_island in other_islands):
                other_island = next(
                    other_island
                    for other_island in other_islands
                    if other_island.x == island.x
                )
                pair = (island, other_island)
                pairs.append(pair)
                if island.value == 2:
                    other_island = next(
                        other_island
                        for other_island in other_islands
                        if other_island.y == island.y
                    )
                    pair = (island, other_island)
                    pairs.append(pair)

            else:
                other_island = next(
                    other_island
                    for other_island in other_islands
                    if other_island.y == island.y
                )
                pair = (island, other_island)
                pairs.append(pair)
        return pairs
