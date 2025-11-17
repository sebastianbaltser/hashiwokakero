from model import Board, Island
from reader import User


class SolvePuzzle:
    def __init__(self, reader: User, console):
        self.reader = reader
        self.console = console

    def __call__(self):
        puzzle = self.reader.read()

        x_max = max(island.x for island in puzzle)
        y_max = max(island.y for island in puzzle)
        board_size = max(x_max, y_max) + 1

        self.board = Board(board_size)

        puzzle = self.solve(puzzle)
        pairs = self.board.create_pairs(puzzle)

        for pair in pairs:
            self.board.draw(pair)

        solution = str(self.board)
        self.console.print(solution)

    def solve(self, puzzle: set[Island]):
        for island in puzzle:
            other_islands = puzzle.copy()
            other_islands.remove(island)
            other_islands = {
                island for island in other_islands if island.remaining_value
            }

            for i in range(island.remaining_value):
                if any(
                    island.is_vertically_aligned(other_island)
                    and other_island not in island.connected_islands
                    for other_island in other_islands
                ):
                    other_island = next(
                        other_island
                        for other_island in other_islands
                        if island.is_vertically_aligned(other_island)
                    )

                elif any(
                    island.is_horizontally_aligned(other_island)
                    and other_island not in island.connected_islands
                    for other_island in other_islands
                ):
                    other_island = next(
                        other_island
                        for other_island in other_islands
                        if island.is_horizontally_aligned(other_island)
                    )

                else:
                    assert False, "remaining value but no aligned islands left"

                other_islands.remove(other_island)
                island.build_bridge(other_island)

        return puzzle
