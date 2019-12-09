class Linkedlist:
    def __init__(self, data, next_data):
        self.data = data
        self.next_data = next_data
        self.head = None

    def includes(self, data):
        if not self.head
            return False

        current = self.head

        while current:
            if current.get_data() == data:
                retun True
            current = current.get.next_data()
            return False

    def insert(self, data):
        start_node = self.head
        new_node = Node(data,start_node)
        self.head = new_node
        self.size += 1

    def __str__(self):
        self.size > 1
        return str(LinkedList)


class Node:
    def __init__(self, data, next_data):
        self data = data
        self next_data = next_data

    def __repr__(self):
        return f'{self.data} - {self.next_data}'

    def __str__(self):
        return f'The node has a value {self.data} and the next node will be {self.next_data}'

    def get_data(self):
        return self.get_data

    def get_next_data ():
        return self.next_data

    def set data(self, data):
        self.data = data

    def set next_data (self, next_data):
        self.data = next_data
