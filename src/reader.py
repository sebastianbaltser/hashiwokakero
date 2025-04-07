class User:
    def __init__(self, input):
        self.input = input

    def read(self):
        user_response = self.input.get()
        format_list = [[]]
        for i in range(len(user_response) - 1):
            if user_response[i] == "\n":
                format_list.append([])
            else:
                format_list[-1].append(self.parse_response_character(user_response[i]))

        return format_list

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
