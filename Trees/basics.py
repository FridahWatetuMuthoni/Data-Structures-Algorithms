class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def insert(self,data):
        new_node = Node(data)
        if(self.is_empty()):
            self.root = new_node
        else:
            current = self.root
            while(current is not None):
                if(data < current.data):
                    if(current.left is None):
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if(current.right is None):
                        current.right = new_node
                        break
                    current = current.right
        self.size += 1
    
    def search(self,target):
        current = self.root
        while(current != None):
            if(target == current.data):
                return True
            if(target > current.data):
                current = current.right
            else:
                current = current.left
        return False
    
    def min_value(self):
        current = self.root
        while(current.left is not None):
            current = current.left
        return current.data
    
    def max_value(self):
        current = self.root
        while(current.right is not None):
            current = current.right
        return current.data
    
    def delete(self,target):
        self.size -= 1
    
    def traverse(self,node):
        pass
    
    ##uses a queue
    def bfs(self):
        pass
    
    def dfs(self):
        pass
    
    def inorder(self):
        pass
    
    def preorder(self):
        pass
    
    def postorder(self):
        pass