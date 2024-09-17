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
        
        if(self.is_empty()):
            self.root  = new_node
        else:
            current = self.root
            while(current is not None):
                if(data < current.data):
                    if(current.left is None):
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
        current = self.root
        while(current is not None):
            if current.data == target:
                return True
            if(target < current.data):
                current = current.left
            else:
                current = current.right
        return False
    
    def min(self):
        current = self.root
        while(current.left is not None):
            current = current.left
        return current.data
    
    def max(self):
        current = self.root
        while(current.right is not None):
            current = current.right
        return current.data
    
    #Depth First Search
    #LROOTR
    def inorder(self):
        results = []
        def traverse(node):
            if(node.left):
                traverse(node.left)
                
            results.append(node.data)
            
            if(node.right):
                traverse(node.right)
        traverse(self.root)
        return results
    
    #ROOTLR
    def preorder(self):
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
        results = []
        
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            results.append(node.data)
        
        traverse(self.root)
        return results
    
    #Breadth First Search
    def bfs(self):
        results = []
        queue = []
        
        queue.append(self.root)
        
        while(len(queue) > 0):
            current = queue.pop(0)
            results.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return results
    
    def delete(self, target):
        #check if the bst is empty
        if(self.is_empty()):
            return 'The Binary Search Tree is empty'
        
        #initialise the parent and current
        parent = None
        current = self.root
        
        #find the node to delete
        while(current is not None and target != current.data):
            parent = current
            if target < current.data:
                current = current.left
            else:
                current = current.right
        
        #check if the target was found or not
        if current is None:
            return "Node was not found in the tree"
        
        # Case One: no children its a leaf node
        if(current.left is None and current.right is None):
            if(self.root == current):
                self.root = None
            else:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
        # Case Two: it has two children
        elif(current.left and current.right):
            succesor_parent = current
            succesor = current.right
            while(succesor.left is not None):
                succesor_parent = succesor
                succesor = succesor.left
            #swap the data
            current.data = succesor.data
            
            #delete the succesor
            if succesor_parent.left == succesor:
                succesor_parent.left = succesor.right
            else:
                succesor_parent.right = succesor.right
        #Case Three: it has one child
        else:
            child = None
            if current.left:
                child = current.left
            if current.right:
                child = current.right
            
            if current == self.root:
                self.root = child
            elif parent.left == current:
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
