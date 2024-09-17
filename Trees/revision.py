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
    
    def delete_node(self, target):
        #check if the bst is empty
        if(self.is_empty()):
            return 'The binary search tree is empty'
        
        #parent and current initialization
        parent = None
        current = self.root
        
        #find the node to delete
        while current != None and current.data != target:
            parent = current
            if(target < current.data):
                current = current.left
            else:
                current = current.right
        
        #check if the node was found
        if current is None:
            return None
        
        #if the node found is a leaf node
        if current.left is None and current.right is None:
            if self.root == current:
                self.root = None
            else:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
        #if the node has both left and right children
        elif(current.left and current.right):
            succesor_parent = current
            succesor = current.right
            #find the minimum value on the right side
            while succesor.left is not None:
                succesor_parent = succesor
                succesor = succesor.left
            #swap the minimum data found with the current node to delete
            current.data = succesor.data
            #delete the minimum node found
            if succesor_parent.left == succesor:
                succesor_parent.left = succesor.right
            else:
                succesor_parent.right = succesor.right
        #else , if node has only one child
        else:
            child = None
            if current.left:
                child = current.left
            else:
                child = current.right
            if current is self.root:
                self.root = child
            else:
                if parent.left == current:
                    parent.left = child
                else:
                    parent.right = child
        self.size -= 1