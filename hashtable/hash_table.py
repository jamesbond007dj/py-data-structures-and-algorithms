class _Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None


    def insert(self, key, value):
        node = _Node(key, value)
        node.next = self.head
        self.head = node

    def includes(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return False


class HashTable:

    def __init__(self, size):
        self.array = [0 for i in range(size)]
        self.size = size


    def hash(self, key):

        key_elements = list(str(key))

        element_sum = 0

        for element in key_elements:
            element_sum += ord(element)

        index = (element_sum * 599) % self.size

        return index


    def add(self, key, value):
        index = self.hash(key)

        if self.array[index] == 0:
            llst = LinkedList()
            llst.insert(key, value)
            self.array[index] = llst
        else:
            llst = self.array[index]

            if llst.includes(key):
                return "This key is already in use, please use another one"
            else:
                llst.insert(key, value)

    def get(self, key):
        index = self.hash(key)

        if self.array[index] != 0 and self.array[index].includes(key):
            return self.array[index].includes(key)
        else:
            return None


    def contains(self, key):
        index = self.hash(key)

        if self.array[index] != 0 and self.array[index].includes(key):
            return True
        else:
            return False

