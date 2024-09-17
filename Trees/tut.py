"""
Binary Search Tree Property
every left child should be less than the parent node and every right child
should be greater than the parent
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = None
    
    def is_empty(self):
        return self.size == 0
    
    def insert(self,data):
        new_node = Node(data)
        
        if self.is_empty():
            self.root = new_node
        else:
            current = self.root
            while(current is not None):
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
        self.size += 1
    
    #LROOTR
    def inorder(self):
        results = []
        
        def traverse(node):
            if node.left:
                traverse(node.left)
            results.append(node.data)
            if node.right:
                traverse(node.right)
        
        traverse(self.root)
        return results
    
    def invert_binary_search_tree(self):
        def traverse(node):
            node.left, node.right = node.right, node.left
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
    
    def check_if_tree_is_balanced(self):
        def check_balance_and_height(node):
            if node is None:
                return (True, 0)  # (is_balanced, height)
                
            left_balanced, left_height = check_balance_and_height(node.left)
            right_balanced, right_height = check_balance_and_height(node.right)
                
            is_balanced = (left_balanced and right_balanced and abs(left_height - right_height) <= 1)
            height = max(left_height, right_height) + 1
                
            return (is_balanced, height)
            
        is_balanced, _ = check_balance_and_height(self.root)
        return is_balanced


bst = BinarySearchTree()
bst.insert(15)
bst.insert(3)
bst.insert(36)
bst.insert(2)
bst.insert(12)
bst.insert(28)
bst.insert(39)

#check if its a valid binary tree
def validate_binary_search_tree():
    arr = bst.inorder()
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

# Before inversion
is_a_valid_binary_tree = validate_binary_search_tree()
print("Is valid before inversion:", is_a_valid_binary_tree)  # Expected: True

# Invert the tree
bst.invert_binary_search_tree()

# After inversion
is_a_valid_binary_tree = validate_binary_search_tree()
print("Is valid after inversion:", is_a_valid_binary_tree)  # Expected: False

#check if the binary tree is balanced

print(bst.check_if_tree_is_balanced())