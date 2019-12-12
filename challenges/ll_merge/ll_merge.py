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

    def __str__(self):
        output = ''
        node = self.head

        while node != None:
            output += f'{node.get_value()}'
            node = node.get_next()

        return output.strip()

    def return_list(self):
        current = self.head
        collection_of_values = []
        while current:
            collection_of_values.append(str(current))
            current = current.next
        return collection_of_values

    
def merge_lists(ll_one, ll_two):
    current_one = ll_one.head
    current_two = ll_two.head

    while current_one !=None and current_two:
        one_next = current_one.next
        two_next = current_two.next

        current_one.next = current_two
        current_two.next = one_next

        current_one = one_next
        current_two = two_next
    return ll_one.head

    