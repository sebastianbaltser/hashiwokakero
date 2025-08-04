from enum import IntEnum


class BridgeType(IntEnum):
    SINGLE = 1


class Board:
    def __init__(self):
        self._board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def draw(self, pair):
        if pair[0].x == pair[1].x:
            self.draw_vertical(pair)
        else:
            self.draw_horizontal(pair)

    def draw_horizontal(self, pair):
        assert pair[2] == BridgeType.SINGLE
        left, right = sorted(pair[:2], key=lambda i: i.x)

        assert pair[0].y == pair[1].y
        row = self._board[pair[0].y]
        assert row[1] == " "
        row[left.x] = str(left.value)
        row[1] = "-"
        row[right.x] = str(right.value)

    def draw_vertical(self, pair):
        assert pair[2] == BridgeType.SINGLE
        bottom, top = sorted(pair[:2], key=lambda i: i.y)

        assert pair[0].x == pair[1].x
        x = pair[0].x

        self._board[top.y][x] = str(top.value)
        assert self._board[1][x] == " "
        self._board[1][x] = "|"
        self._board[bottom.y][x] = str(bottom.value)

    def __str__(self):
        rows = ["".join(row) for row in self._board]
        rows = reversed(rows)
        return "\n".join(rows) + "\n"


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
