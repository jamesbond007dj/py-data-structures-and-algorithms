class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value} - {self.next}'

    def __str__(self):
        return f'The current node has a value {self.value}, and the next node is {self.next}'

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next