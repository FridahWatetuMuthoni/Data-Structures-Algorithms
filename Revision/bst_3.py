class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def insert(self,data):
        new_node = Node(data)
        
        if self.is_empty():
            self.root = new_node
        else:
            current = self.root
            while current is not None:
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
    
    def search(self,target):
        if self.is_empty():
            return 'The Binary Search Tree is empty'
        
        current = self.root
        
        while current is not None:
            if current.data == target:
                return True
            if target < current.data:
                current = current.left
            else:
                current = current.right
        return False
    
    def max(self):
        if self.is_empty():
            return 'The Binary Search Tree is empty'
        
        current = self.root
        
        while current.right is not None:
            current = current.right
        
        return current.data
    
    def min(self):
        if self.is_empty():
            return 'The Binary Search Tree is empty'
        
        current = self.root
        
        while current.left is not None:
            current = current.left
        
        return current.data
    
    #LROOTR
    def inorder(self):
        if self.is_empty():
            return 'The Binary Search Tree is empty'
        
        results = []
        
        def traverse(node):
            if node.left:
                traverse(node.left)
            
            results.append(node.data)
            
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results
            
    #ROOTLR
    def preorder(self):
        if self.is_empty():
            return 'The Binary Search Tree is empty'
        
        results = []
        
        def traverse(node):
            results.append(node.data)
            
            if node.left:
                traverse(node.left)
                        
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results
    
    #LRROOT
    def postorder(self):
        if self.is_empty():
            return 'The Binary Search Tree is empty'
        
        results = []
        
        def traverse(node):
            if node.left:
                traverse(node.left)
                        
            if node.right:
                traverse(node.right)
            
            results.append(node.data)
        traverse(self.root)
        return results
    
    def bfs(self):
        if self.is_empty():
            return 'The Binary Search Tree is empty'
        
        results = []
        queue = []
        
        queue.append(self.root)
        
        while len(queue) > 0:
            current = queue.pop(0)
            
            results.append(current.data)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return results
    
    def check_is_balanced(self):
        if self.is_empty():
            return 'The Binary Search Tree is empty'
        
        def is_balanced(node):
            if node is None:
                return (True, 0)
            
            left_balanced,left_height = is_balanced(node.left)
            right_balanced, right_height = is_balanced(node.right)
            
            height = max(left_height, right_height) + 1
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            return balanced, height
        
        balanced, height = is_balanced(self.root)
        return balanced
    
    def is_valid(self):
        if self.is_empty():
            return 'The Binary Search Tree is empty'
        
        sorted_array = self.inorder()
        
        for i in range(len(sorted_array) - 1):
            if sorted_array[i + 1] < sorted_array[i]:
                return False
        return True
    
    def invert_tree(self):
        if self.is_empty():
            return 'The Binary Search Tree is empty'
        
        def traverse(node):
            node.left, node.right = node.right, node.left
            
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
    
    def delete(self,target):
        if self.is_empty():
            return 'The Binary Search Tree is empty'
        
        #variables
        current = self.root
        parent = None
        
        #find the node
        while current is not None and current.data != target:
            parent = current
            if target < current.data:
                current = current.left
            else:
                current = current.right
        
        #check if found
        if current is None:
            return 'Node not found'
        
        #delete node
        
        #no children
        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            else:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
        #two children
        elif current.left and current.right:
            #find the successor
            successor_parent = current
            successor = current.right
            
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            
            #swap values
            current.data = successor.data
            
            #delete successor
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        #one child
        else:
            child = None
            if current.left:
                child = current.left
            if current.right:
                child = current.right
            
            if parent == self.root:
                self.root = child
            else:
                if parent.left == current:
                    parent.left = child
                else:
                    parent.right = child
        self.size -= 1



bst = BinarySearchTree()
bst.insert(15)
bst.insert(3)
bst.insert(36)
bst.insert(2)
bst.insert(12)
bst.insert(28)
bst.insert(39)

print("Inorder:", bst.inorder())
# inorder => [2, 3, 12, 15, 28, 36, 39]

print("Preorder:", bst.preorder())
# preorder => [15, 3, 2, 12, 36, 28, 39]

print("Postorder:", bst.postorder())
# postorder => [2, 12, 3, 28, 39, 36, 15]

print("BFS:", bst.bfs())
# bfs => [15, 3, 36, 2, 12, 28, 39]

print("Min:", bst.min())  # Min => 2

print("Max:", bst.max())  # Max => 39

print("Search 10:", bst.search(10))  # Search => False
print("Search 28:", bst.search(28))  # Search => True

print("BFS before deletion:", bst.bfs())
# bfs => [15, 3, 36, 2, 12, 28, 39]

bst.delete(36)
print("BFS after deleting 36:", bst.bfs())
# bfs => [15, 3, 39, 2, 12, 28]


# Before inversion
is_a_valid_binary_tree =bst.is_valid()
print("Is valid before inversion:", is_a_valid_binary_tree)  # Expected: True

# Invert the tree
bst.invert_tree()

# After inversion
is_a_valid_binary_tree = bst.is_valid()
print("Is valid after inversion:", is_a_valid_binary_tree)  # Expected: False

#check if the binary tree is balanced

print(bst.check_is_balanced())