from model import Island


class User:
    def __init__(self, input):
        self.input = input

    def read(self):
        user_response = self.input.get()

        x = 0
        y = 2

        islands = set()

        for el in user_response:
            if el == "\n":
                y -= 1
                x = 0
                continue

            if el == " ":
                x += 1
                continue

            if el.isdigit():
                island = Island(x, y, int(el))
                islands.add(island)
                x += 1
                continue

        return islands

    def parse_response_character(self, response_character):
        return int(response_character) if response_character != " " else None


class Input:
    def get(self):
        return input("Write input: \n")


class StubbedInput:
    def __init__(self, response={Island(1, 2, 1), Island(1, 0, 1)}):
        self.response = response

    def get(self):
        grid = ["   ", "   ", "   "]

        for island in self.response:
            row = grid[island.y]
            new_row = row[: island.x] + str(island.value) + row[island.x + 1 :]
            grid[island.y] = new_row

        result = "\n".join(grid)
        return result + "\n"
