from collections import deque

class _Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, value):
        current = self.front
        new_node = _Node(value)
        if current is None:
            self.front = new_node
        else:
            while current.next:
                current = current.next
                current.next = new_node

    def dequeue(self):
        if self.front == None:
            return None
        else:
            removed_node = self.front
            self.front = self.front.next
            return removed_node.value

    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, value):
        node = _Node(value)
        if not self._root:
            self._root = node
            return
        current = self._root 
        while True:
            if value < current.value:
                if not current.left:
                    current.left = node
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    return
                current = current.right

    def contains(self, value):
        if not self._root:
            return False
        if self._root.value == value:
            return True
        current = self._root 
        while True:
            if value == current.value:
                return True
            if value < current.value:
                if current.left:
                    current=current.left
                else:
                    return False
            if value > current.value:
                if current.right:
                    current=current.right
                else:
                    return False

    def pre_order(self, node=None, arr=[]):
        node = node or self._root
        arr.append(node.value)
        if node.left:
            self.pre_order(node.left, arr)
        if node.right:
            self.pre_order(node.right, arr)
        return arr

    def in_order(self, node=None, arr=[]):
        node = node or self._root
        if node.left:
            self.in_order(node.left, arr)
        arr.append(node.value)
        if node.right:
            self.in_order(node.right, arr)
        return arr

    def post_order(self, node=None, arr=[]):
        node = node or self._root
        
        if node.left:
            self.post_order(node.left, arr)
        
        if node.right:
            self.post_order(node.right, arr)
        arr.append(node.value)
        return arr

    def breadth_first(self, node=None, arr=[]):
        node = node or self._root
        q = Queue()
        q.enqueue(self._root)
        while q.peek():
            node = q.dequeue()
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            arr.append(node.value)
        return arr

class BinarySearchTree(BinaryTree):
    def add(self, value):
        node = _Node(value)
        if not self._root:
            self._root = node
            return
        current = self._root 
        while True:
            if value < current.value:
                if not current.left:
                    current.left = node
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    return
                current = current.right

    def contains(self, value):
        if not self._root:
            return False
        if self._root.value == value:
            return True
        current = self._root 
        while True:
            if value == current.value:
                return True
            if value < current.value:
                if current.left:
                    current=current.left
                else:
                    return False
            if value > current.value:
                if current.right:
                    current=current.right
                else:
                    return False
