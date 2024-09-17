"""
A binary search tree is balanced when the left and right sub tree has roughly the same amount of nodes.
A perfect tree is when the right and left sub tree has the same number of nodes.

Deleting a Node from a binary search tree:

1. Searching for the Node to Delete:
Start at the root of the tree.
If the target node is smaller than the current node, go to the left child.
If the target node is larger, go to the right child.
Repeat until the node is found.

2. Case 1: Node has No Children (Leaf Node):
Once the target node is found, check if it has no children.
If it has no children, simply remove the node by updating the parent’s reference to None.

3. Case 2: Node has One Child:
If the node has only one child (either left or right), replace the node with its child.
The parent of the node now points to the node’s child instead.

4. Case 3: Node has Two Children:
When the node to be deleted has two children, find the in-order successor (the smallest node in the right subtree).
Replace the data of the node to be deleted with the in-order successor's data.

Recursively delete the in-order successor node.
Would you like me to adjust the code or regenerate a clearer image of the tree to match this process?

"""

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
        
        if(self.is_empty()):
            self.root = new_node
        else:
            current  =  self.root
            while(current != None):
                if(data <= current.data):
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
    
    def search(self,target):
        current = self.root
        while(current is not None):
            if(current.data == target):
                return True
            if(current.data < target):
                current = current.right
            else:
                current = current.left
        return False
    
    def delete_iteration(self,target):
        if self.is_empty():
            return 'The BST is empty'
        
        #initialise current and parent
        parent = None
        current = self.root
        
        #find the node to delete
        while(current.data != target and current != None):
            if target < current.data:
                parent = current
                current = current.left
            else:
                current = current.right
        
        #check if the node was found
        if current is None:
            return None
        
        #if the node found is a leaf node
        if current.left is None and current.right is None:
            if current is self.root:
                self.root = None
            else:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
        
        #if the node found has two children
        elif current.left and current.right:
            # Find the inorder successor (minimum node in the right subtree)
            succesor_parent = current
            succesor = current.right
            while succesor.left is not None:
                succesor_parent = succesor
                succesor = succesor.left
        
            #replace the current data with the successors data
            current.data = succesor.data
        
            #delete the successors node
            if succesor_parent.left == succesor:
                succesor_parent.left = succesor.right
            else:
                succesor_parent.right = succesor.right
        
        else:
            #Determine the child
            child = None
            if current.left:
                child = current.left
            else:
                child = current.right
            
            if self.root == current:
                self.root = child
            else:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
        
        self.size -= 1
        
    
    def find_min(self,node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

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
    
    #ROOTLR
    def preorder(self):
        results = []
        
        def traverse(node):
            results.append(node.data)
            if(node.left):
                traverse(node.left)
            if(node.right):
                traverse(node.right)
        traverse(self.root)
        return results
    
    #Breadth First Search
    #uses a queue
    def bfs(self):
        results = []
        queue = []
        queue.append(self.root)
        
        while(len(queue) > 0):
            current_node = queue.pop(0)
            results.append(current_node.data)
            if(current_node.left):
                queue.append(current_node.left)
            if(current_node.right):
                queue.append(current_node.right)
        
        return results

bst = BinarySearchTree()
bst.insert(15)
bst.insert(3)
bst.insert(36)
bst.insert(2)
bst.insert(12)
bst.insert(28)
bst.insert(39)

print(bst.inorder())
#inorder => [2,3,12,15,28,36,39]

print(bst.preorder())
#preorder => [15, 3, 2,12,36,28,29]

print(bst.postorder())
#postorder => [2,12,3,28,39,36,15]

print(bst.bfs())
#bfs => [15,3,36,2,12,28,39]
print(bst.delete(36))
#bfs => [15,3,36,2,12,28,39]
print(bst.bfs())
#bfs => [15,3,36,2,12,28,39]