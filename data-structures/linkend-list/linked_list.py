from node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        value = Node.is_node(value)
        value.next = self.head
        self.head = value
        self._length +=1

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
            if current.next == None
            current.next = Node(value)
            return self.__str__() 
        else:
            current = current.next

    def insert_before(value, next_value):
        if self.includes(value):
            current = self.head
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

        def insert_after(value, next_value):
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