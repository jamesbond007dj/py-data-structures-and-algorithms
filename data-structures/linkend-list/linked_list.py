from node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        

    def includes(self, value):
        if not self.head:
            return False
        current = self.head

        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def to_string(self):
        output = ''
        node = self.head

        while node != None:
            output += f'{node.get_value()}'
            node = node.get_next()

        return output.strip()

    def append(self, value):
        current = self.head
        while current:
            print(current.value)
            if current.next == None:
                current.next = Node(value)
                return self.__str__() 
            else:
                current = current.next
        self.head = Node(value)
        return self.__str__()

    def insert_before(self, value, new_value):
        if self.includes(value):
            current = self.head
            previous = current
            while current:
                if current.value == value:
                    node = Node(new_value)
                    node.next = current
                    previous.next = node
                    return self.__str__() 
                previous = current 
                current = current.next
        else:
            return 'Value is not in the list'

    def insert_after(self, value, new_value):
        if self.includes(value):
            current = self.head
            while current:
                if current.value == value:
                    node = Node(new_value)
                    node.next = current.next
                    current.next = Node 
                    return self.__str__() 
                current = current.next
        else:
            return 'Value is not in the list'