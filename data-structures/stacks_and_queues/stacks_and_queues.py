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


class Stack:

    def __init__(self):
        self.top = None
        

    def __str__(self):
        output = ''
        node = self.top

        while node != None:
            output += f'{node.get_value()}'
            node = node.get_next()

        return output.strip()


    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        return self.top

    def pop(self):
        if self.top == None:
            return
        current = self.top
        self.top = current.next
        return current.value  

        
    def peek(self):
        if self.top ==None:
            return 
        else:
            return self.top.value


    def is_empty(self):
        current = self.top
        if current !=None:
            return False
        else:
            return True


class Queue:

    def __init__(self):
        self.rear = None
        self.front = None
        self.queue = []
        self.size = 0

    def __str__(self):
        output = ''
        node = self.rear

        while node != None:
            output += f'{node.get_value()}'
            node = node.get_next()

        return output.strip()

    def enqueue(self, value):
        node = Node(value)
        node.next = self.rear
        self.rear = node
        if not self.front:
            self.front = self.rear
        

    def dequeue(self):
        if not self.front:
            raise EmptyQueueException('Empty')
        else:
            node = self.front
            self.front = node.next
            node.next = None
            

    def peek(self):
        if self.rear == None:
            return 
        else:
            current = self.rear
            current = current.next
            if current.next == None:
                current = self.front
            return current.value

    def is_empty_queue(self):
        current = self.rear
        if current !=None:
            return False
        else:
            return True