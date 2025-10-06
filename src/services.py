from model import Board, BridgeType


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

            if any(
                island.is_vertically_aligned(other_island)
                for other_island in other_islands
            ):
                other_island = next(
                    other_island
                    for other_island in other_islands
                    if island.is_vertically_aligned(other_island)
                )
                pair = (island, other_island, BridgeType.SINGLE)
                if (other_island, island, BridgeType.SINGLE) not in pairs:
                    pairs.append(pair)

                if island.value == 2:
                    other_island = next(
                        other_island
                        for other_island in other_islands
                        if island.is_horizontally_aligned(other_island)
                    )

                    pair = (island, other_island, BridgeType.SINGLE)
                    if (other_island, island, BridgeType.SINGLE) not in pairs:
                        pairs.append(pair)

            else:
                other_island = next(
                    other_island
                    for other_island in other_islands
                    if island.is_horizontally_aligned(other_island)
                )
                pair = (island, other_island, BridgeType.SINGLE)
                if (other_island, island, BridgeType.SINGLE) not in pairs:
                    pairs.append(pair)
        return pairs
