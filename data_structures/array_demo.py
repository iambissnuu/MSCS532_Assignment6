class ArrayDemo:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, value):
        if value in self.data:
            self.data.remove(value)

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return None

    def traverse(self):
        return self.data
