class User:
    def read(self):
        return [[None, 1, None], [None, None, None], [None, 1, None]]

    def __init__(self, input):
        self.input = input


class Input:
    def get(self):
        return input("Write input: \n")


class StubbedInput:
    def get(self):
        return " 1 \n   \n 1 \n"
