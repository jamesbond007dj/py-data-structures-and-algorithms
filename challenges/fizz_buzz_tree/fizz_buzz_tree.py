import pytest

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.next = None 
        self.left = left
        self.right = right

    
class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value, root=None):
        node = Node(value)
        root = root or self.root

        if not root:
            self.root = node
            return

        if value < root.value:
            if root.left:
                self.add(value, root.left)
            else:
                root.left = node
        if value > root.value:
            if root.right:
                self.add(value, root.right)
            else:
                root.right = node
    
    def pre_order(self, node = None, result = []):
        node = node or self.root        

        result.append(node.value)

        if node.left:
            self.pre_order(node.left, result)

        if node.right:
            self.pre_order(node.right, result)

        return result
    
    def in_order(self, node = None, result = []):

        node = node or self.root

        if node.left:
            self.pre_order(node.left, result)
        result.append(node.value)

        if node.right:
            self.pre_order(node.right, result)

        return result        

    def post_order(self, node = None, result = []):

        node = node or self.root

        if node.left:
            self.pre_order(node.left, result)


        if node.right:
            self.pre_order(node.right, result)
        result.append(node.value)

        return result    

    
    
class BinarySearchTree(BinaryTree):
    def add(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        current = self.root
        
        while current:
            if value > current.value:

                if not current.right:
                    current.right = node
            else:

                if not current.left:
                    current.left = node
            return

    def contains(self, value):
        current = self.root

        if current.value == value:
            return True
        
        if value > current.value:
            if current.right.value == value:
                return True
        else:

            if current.left.value == value:
                return True

        return False
    
    
def fizz_buzz_tree(tree):
    new_tree = BinaryTree()
    def fizzyfy (num):
        adjusted_value =''
        if num % 3 == 0:
           adjusted_value += 'Fizz'
        if num % 5 == 0:
            adjusted_value += 'Buzz'
        
        return adjusted_value or str(num)
        
    
    def traverse (root):
        if not root:
            return None
        fizzified = fizzyfy(root.value)
        node = Node(fizzified)
        node.left = traverse(root.left)
        node.right = traverse(root.right)
        return node

    new_tree.root = traverse(tree.root)
    return new_tree