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

        
    def peek(self, k):
        if k < 0:
            return 'Negative k has no value'
        else:
            current = self.top
            count=0
            while current.next:
                current= current.next
                count += 1
            current=self.top
            if k > count:
                return 'No value'
            for k in range(count - k):
                current = current.next
            return current.value


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
        return self.rear

    def dequeue(self):
        if self.rear == None:
            return
        else:
            node = self.front
            self.front = self.front.next
            self.next = None
            self.size -=1
            return node

    def peek(self):
        if self.rear == None:
            return 
        else:
            current = self.rear
            current = current.next
            if current.next == None:
                current = self.front
            return current

    def is_empty_queue(self):
        current = self.rear
        if current !=None:
            return False
        else:
            return True