class Node:
    def __init__(self, x, next_node=None):
        self.value = x
        self.next = next_node


class Dog:
    def __init__(self, type=None):
        self.type = 'dog'


class Cat:
    def __init__(self, type=None):
        self.type = 'cat'


class FifoAnimalShelter:
    def __init__(self, top=None):
        self.top = top
        self.st_1 = Stack()
        self.st_2 = Stack()

    def enqueue(self, animal):
        if animal.type !='dog' or 'cat':
            return 'we can only accept cat or dog'
        else:
            node = Node(animal)
            while self.st_1.top:
                self.st_2.push(self.st_1.pop())
            self.st_2.push(node)
            while self.st_2.top:
                self.st_1.push(self.st_2.pop())

    def dequeue(self, pref):
        if not self.st_1.top:
            return 'Sorry we have no animal left to be adopted'
        results = None
        while self.st_1.top:
            node = self.st_1.top
            if node.data.type != pref:
                self.st_2.push(node)
            else:
                results= node.data
                break
        while self.st_2.top:
            self.st_1.push(self.st_2.pop())
        return results
          
