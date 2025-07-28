class Board:
    def __init__(self, board_string):
        self.board_string = board_string

    def draw(self, pair):
        if pair[0].x == pair[1].x:
            self.draw_vertical(pair)
        else:
            self.draw_horizontal(pair)

    def draw_horizontal(self, pair):
        left, right = sorted(pair, key=lambda i: i.x)

        assert pair[0].y == pair[1].y
        line_index = 8 - 4 * pair[0].y
        self.board_string = (
            self.board_string[:line_index]
            + f"{left.value}-{right.value}"
            + self.board_string[line_index + 3 :]
        )

    def draw_vertical(self, pair):
        bottom, top = sorted(pair, key=lambda i: i.y)

        assert pair[0].x == pair[1].x
        x = pair[0].x
        self.board_string = (
            self.board_string[:x] + f"{top.value}" + self.board_string[x + 1 :]
        )
        self.board_string = (
            self.board_string[: x + 4] + "|" + self.board_string[x + 1 + 4 :]
        )
        self.board_string = (
            self.board_string[: x + 8]
            + f"{bottom.value}"
            + self.board_string[x + 1 + 8 :]
        )


class Island:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return f"Island(x={self.x!r}, y={self.y!r}, value={self.value!r})"

    def __eq__(self, other):
        if isinstance(other, Island):
            return self.x == other.x and self.y == other.y and self.value == other.value
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.value))
