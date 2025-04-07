class User:
    def __init__(self, input):
        self.input = input

    def read(self):
        user_response = self.input.get()
        if "2" in user_response:
            return [[None, 2, None], [None, None, None], [None, 2, None]]
        elif "3" in user_response:
            return [[None, 3, None], [None, None, None], [None, 3, None]]
        else:
            return [[None, 1, None], [None, None, None], [None, 1, None]]


class Input:
    def get(self):
        return input("Write input: \n")


class StubbedInput:
    def __init__(self, response=" 1 \n   \n 1 \n"):
        self.response = response

    def get(self):
        return self.response
