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
    
    def insert(self,data):
        new_node = Node(data)
        self.size += 1
        if(self.is_empty()):
            self.root = new_node
        else:
            current = self.root
            while(current != None):
                if(data < current.data):
                    #go left
                    if(current.left is None):
                        current.left = new_node
                        break
                    current = current.left
                else:
                    #go right
                    if(current.right is None):
                        current.right = new_node
                        break
                    current = current.right
    
    def maximum(self):
        if self.is_empty():
            return None
        
        current = self.root
        while(current.right != None):
            current = current.right
        return current.data
    
    def minimum(self):
        if self.is_empty():
            return None
        
        current = self.root
        while(current.left != None):
            current = current.left
        return current.data
    
    def search(self,value):
        if self.is_empty():
            return None
        
        current = self.root
        while(current != None):
            if(current.data == value):
                return True
            if(value < current.data):
                current = current.left
            else:
                current = current.right
        return False
    
    
    def delete(self, value):
        if self.is_empty():
            return None
        
        # Start with the root node and initialize parent as None
        parent = None
        current = self.root
        
        # Find the node to be deleted and its parent
        while current and current.data != value:
            parent = current
            if value < current.data:
                current = current.left
            else:
                current = current.right
        
        # If the node was not found
        if current is None:
            return None
        
        # Case 1: Node to be deleted has no children (leaf node)
        if current.left is None and current.right is None:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        
        # Case 2: Node to be deleted has two children
        elif current.left and current.right:
            # Find the inorder successor (minimum node in the right subtree)
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            # Replace current's data with successor's data
            current.data = successor.data
            
            # Delete the successor node (which will have at most one child)
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        
        # Case 3: Node to be deleted has one child
        else:
            # Determine the child
            child = current.left if current.left else current.right
            
            if current != self.root:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
        
        self.size -= 1

    
    #DFS => stack
    def inorder(self):
        pass
    
    def preorder(self):
        pass
    
    def postorder(self):
        pass
    
    def dfs(self):
        pass
    
    def bfs(self):
        pass