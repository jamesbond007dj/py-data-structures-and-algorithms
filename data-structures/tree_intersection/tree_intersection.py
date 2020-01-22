def tree_intersection(tree_1, tree_2):
    tree_set = set()
    result = []
   
    def check_tree_1(node):
        
        nonlocal result
        if node is None:
            return 
        tree_set.add(node.value)
        check_tree_1(node.left)
        check_tree_1(node.right)
    check_tree_1(tree_1.root)
   
    def check_tree_2(node):
        
        nonlocal tree_set
        nonlocal result
        if node is None:
            return
        if node.value in tree_set:
            result.append(node.value)
        check_tree_2(node.left)
        check_tree_2(node.right)
    check_tree_2(tree_2.root)
    return result