## Trees
The goal fo this code challenge is to make a data tree class

## Challenge
Using Node Class, BinaryTree Class and BinarySearchTree Class creating Tree with add function, by contains function find a value in a tree, returns True if the value is in the tree or returns False if the value is not in the tree, then return collections by pre order, in order and post order traversals.  

## Approach & Efficiency
Binary Search Tree
Add: Time O(h) Space: O(n)
Contains: Time O(h) Space O(n)

## APIs
Binary Search Tree:
Add: In Value -> Out: None
Contains: In Value -> Out: True/False
Display Functions: In None -> Out: List
preOrder(root)
    // INPUT <-- root node
    // OUTPUT <-- pre-order output of tree nodes
### OUT <-- root.value 
    if root.left is not NULL preOrder(root.left)
    if root.right is not NULLpreOrder(root.right)
inOrder(node)
    // INPUT <-- root node
    // OUTPUT <-- in-order output of tree nodes
    if node.left is not NULL inOrder(node.left) 
### OUTPUT <-- node.value
    if node.right is not NULL inOrder(node.right)
postOrder(node)
    // INPUT <-- root node
    // OUTPUT <-- post-order output of tree nodes
    if node.left is not NULL inOrder(node.left)
    if node.right is not NULL inOrder(node.right)
### OUTPUT <-- node.value