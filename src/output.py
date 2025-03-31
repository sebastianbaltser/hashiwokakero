class Console:
    def __init__(self):
        self.output = []

    def print(self, text):
        self.output.append(text)
        print(text)

    def track_output(self):
        return self.output
