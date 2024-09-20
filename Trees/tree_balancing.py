"""
A balanced binary tree is defined as a binary tree in which at every node,
its left sub-tree and right sub-tree have an equal height or their height differ by just 1.

Algorithm CheckBalancedBinaryTree:
Input: Root Node of the binary tree.
Output:True if binary tree is balanced and False otherwise.

Start.
0.If tree is empty, return True.
1. Check the height of left sub-tree.
2.Check the height of right sub-tree.
3.If difference in height is greater than 1 return False.
4.Check if left sub-tree is balanced.
5.Check if right sub-tree is balanced.
6. If left sub-tree is balanced and right sub-tree is also balanced, return True.
End

Algorithm height(tree):
Input: Root of the tree
Output: Height of the tree
Start.
1.If the root is None, Return 0.
2.Find the height of the left subtree.//height(root.leftChild)
3.Find the height of the right subtree .//height(root.rightChild)
4.Find the maximum value in 2 and 3 and add 1 to it.
End
Now we will implement the above algorithm and execute it for the following binary tree.

"""

#find the height of a binary tree
#we are using depth first search

def height(node):
    
    if node is None:
        return 0
    
    left_height = height(node.left)
    right_height = height(node.right)
    
    return max(left_height, right_height) + 1

def check_if_balanced(root):
    
    def is_balanced(node):
        if node is None:
            return (True, 0)
        
        left_balanced, left_height = is_balanced(node.left)
        right_balanced, right_height = is_balanced(node.right)
        
        height = max(left_height, right_height) + 1
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        
        return (balanced, height)
    
    balanced, height = is_balanced(root)
    return balanced

