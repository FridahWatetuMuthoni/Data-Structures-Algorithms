"""
write a recursive function that given an input  sums all nonnegative intergers upto n
"""

def sum(n , total = 0):
    #base case
    if(n == 0 ):
        return total
    total+= n
    return sum(n-1,total)

print(sum(5))

def total(n):
    if n == 0:
        return 0
    return n + total(n-1)

"""
Write a function that takes two inputs n and m and outputs the number of unique paths from the top left corner to 
bottom right corner of a n x m grid.You can only move down or right  unit at a time.
"""

def possible_paths(n,m):
    if n == 0 or m == 0:
        return 1
    return possible_paths(n,m-1) + possible_paths(n-1,m)

"""
find the number of leaf nodes in a binary tree
"""

def number_of_leaf_nodes(node):
    #base case
    if(node == None):
        return 0
    if(node.left == None and node.right == None):
        return 1
    return number_of_leaf_nodes(node.left) + number_of_leaf_nodes(node.right)

