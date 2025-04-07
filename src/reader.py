class User:
    def __init__(self, input):
        self.input = input

    def read(self):
        user_response = self.input.get()

        number_1 = int(user_response[1]) if user_response[1] != " " else None
        number_2 = int(user_response[9])

        return [[None, number_1, None], [None, None, None], [None, number_2, None]]


class Input:
    def get(self):
        return input("Write input: \n")


class StubbedInput:
    def __init__(self, response=" 1 \n   \n 1 \n"):
        self.response = response

    def get(self):
        return self.response
