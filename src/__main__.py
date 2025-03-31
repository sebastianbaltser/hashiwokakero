from services import SolvePuzzle
from output import Console
from reader import Input, User


def main():
    input = Input()
    reader = User(input)
    output = Console()
    app = SolvePuzzle(reader, output)
    app()


if __name__ == "__main__":
    main()
