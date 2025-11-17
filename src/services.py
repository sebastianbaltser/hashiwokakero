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
        self.board.draw(puzzle)

        solution = str(self.board)
        self.console.print(solution)

    def solve(self, puzzle: set[Island]):
        for island in puzzle:
            other_islands = puzzle.copy()
            other_islands.remove(island)
            vertically_aligned_islands = {
                other for other in other_islands if island.is_vertically_aligned(other)
            }
            up_neighbours = {
                other for other in vertically_aligned_islands if island.y < other.y
            }
            down_neighbours = {
                other for other in vertically_aligned_islands if other.y < island.y
            }
            up_neighbour = min(
                up_neighbours, key=lambda other: abs(other.y - island.y), default=None
            )
            down_neighbour = min(
                down_neighbours, key=lambda other: abs(other.y - island.y), default=None
            )

            horizontally_aligned_islands = {
                other
                for other in other_islands
                if island.is_horizontally_aligned(other)
            }
            left_neighbours = {
                other for other in horizontally_aligned_islands if island.x < other.x
            }
            right_neighbours = {
                other for other in horizontally_aligned_islands if other.x < island.x
            }
            left_neighbour = min(
                left_neighbours, key=lambda other: abs(other.x - island.x), default=None
            )
            right_neighbour = min(
                right_neighbours,
                key=lambda other: abs(other.x - island.x),
                default=None,
            )

            neighbours = set()
            for neighbour in {
                up_neighbour,
                down_neighbour,
                left_neighbour,
                right_neighbour,
            }:
                if neighbour is not None and 0 < neighbour.remaining_value:
                    neighbours.add(neighbour)

            other_islands = neighbours

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
