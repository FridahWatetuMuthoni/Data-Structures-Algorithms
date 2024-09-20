class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def insert(self, data):
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
    
    def search(self, target):
        current  = self.root
        
        while current is not None:
            if current.data == target:
                return True
            if target < current.data:
                current = current.left
            else:
                current = current.right
        return False
    
    def max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data
    
    def min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data
    
    #depth first search
    
    #inorder=>LROOTR
    def inorder(self):
        results = []
        
        def traverse(node):
            if node.left:
                traverse(node.left);
                
            results.append(node.data)
            
            if node.right:
                traverse(node.right)
                
        traverse(self.root)
        return results
    
    #preorder=>ROOTLR
    def preorder(self):
        results = []
        
        def traverse(node):
            results.append(node.data)

            if node.left:
                traverse(node.left);
            
            if node.right:
                traverse(node.right)
                
        traverse(self.root)
        return results
    
    #postorder=>LRROOT
    def postorder(self):
        results = []
        
        def traverse(node):
            if node.left:
                traverse(node.left);
            
            if node.right:
                traverse(node.right)
                
            results.append(node.data)

        traverse(self.root)
        return results
    
    #breadth first search
    def bfs(self):
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
    
    def tree_is_balanced(self):
        def is_balanced(node):
            if node is None:
                return (True, 0)
            
            left_balanced, left_height = is_balanced(node.left)
            right_balanced, right_height = is_balanced(node.right)
            
            height = max(left_height, right_height) + 1
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            return balanced, height
        balanced, height = is_balanced(self.root)
        
        return balanced
    
    def validated_tree(self):
        arr = self.inorder()
        
        for i in range(len(arr)-1):
            if arr[i +1] < arr[i]:
                return False
        return True 
    
    def invert_binary_search_tree(self):
        def traverse(node):
            node.left, node.right = node.right, node.left
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
    
    def delete(self, target):
        #check if its empyt
        if self.is_empty():
            return 'The Binary search tree is empty'
        
        #initialise variables
        parent = None
        current = self.root
        
        #find the node to delete
        
        while(current is not None and current.data != target):
            parent = current
            if target < current.data:
                current = current.left
            else:
                current = current.right
        
        #check if we found the node
        if current is None:
            return f"{target} was not found"  
              
        #delete the found node
        #if the node has no children
        if current.right is None and current.left is None:
            if current == self.root:
                self.root = None
            else:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
        #if it has two children
        elif current.left and current.right:
            #find the successor on the right side of the current node
            successor_parent = current
            successor = current.right
            while successor.left is not None:
                successor = successor.left
            
            #swap the values
            current.data = successor.data
            
            #delete the successor node
            if successor_parent.right == successor:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right
        #if it has one child
        else:
            child = None
            if current.left:
                child = current.left
            if current.right:
                child = current.right
            
            if self.root == parent:
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
is_a_valid_binary_tree =bst.validated_tree()
print("Is valid before inversion:", is_a_valid_binary_tree)  # Expected: True

# Invert the tree
bst.invert_binary_search_tree()

# After inversion
is_a_valid_binary_tree = bst.validated_tree()
print("Is valid after inversion:", is_a_valid_binary_tree)  # Expected: False

#check if the binary tree is balanced

print(bst.tree_is_balanced())