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
