class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Animal:
   def __init__(self, type=None):
       self.type = None
        

class Dog(Animal):
    def __init__(self, type=None):
        self.type = 'dog'


class Cat(Animal):
    def __init__(self, type=None):
        self.type = 'cat'


class Stack:
  def __init__(self, top = None):
    self.top = top

  def push(self, value):
    next_top = Node(value)
    self.top = next_top

  def pop(self):
    if not isinstance(self.top, Node):
        print('Empty List')
    st_2 = self.top
    self.top = self.top.next
    return st_2.value

  def peek(self):
    if isinstance(self.top, Node):
      return self.top.value
    

  def is_empty(self):
    if self.top:
      return False
    return True

class FifoAnimalShelter:
    def __init__(self, top=None):
        self.top = top
        self.st_1 = Stack()
        self.st_2 = Stack()

    def enqueue(self, animal):
        if animal.type.lower() !='dog' or 'cat':
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
          
