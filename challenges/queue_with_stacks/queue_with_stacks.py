class Node:
  def __init__(self, x, next_node = None):
    self.value = x
    self.next = next_node

class Stack:
  def __init__(self, top = None):
    self.top = top

  def push(self, value):
    next_top = Node(value, self.top)
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

class PseudoQueue:
  def __init__(self):
    self.stack = Stack()

  def enqueue(self, x):
    self.stack.push(x)

  def dequeue(self):
    st_1 = Stack()
    while self.stack.top:
      st_1.push(self.stack.pop())
    st_2 = st_1.pop()
    while st_1.top:
      self.enqueue(st_1.pop())
    return st_2


