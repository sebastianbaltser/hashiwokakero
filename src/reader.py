class User:
    def __init__(self, input):
        self.input = input

    def read(self):
        user_response = self.input.get()

        number_1 = self.parse_response_character(user_response[0])
        number_2 = self.parse_response_character(user_response[1])
        number_8 = self.parse_response_character(user_response[9])

        return [[number_1, number_2, None], [None, None, None], [None, number_8, None]]

    def parse_response_character(self, response_character):
        return int(response_character) if response_character != " " else None


class Input:
    def get(self):
        return input("Write input: \n")


class StubbedInput:
    def __init__(self, response=" 1 \n   \n 1 \n"):
        self.response = response

    def get(self):
        return self.response
