class User:
    def read(self):
        return self.input.get()
    
    def __init__(self, input):
        self.input = input
        
class Input:
    def get(self):
        return input("Write input: \n")

class StubbedInput:
    def get(self):
        return (
            " 1 \n"
            "   \n"
            " 1 \n"
        )