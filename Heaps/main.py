"""
A heap is a  maximally efficient implementation of the priority queue abstract data type.
finding nodes.
Using Index: beacause it starts at 0
Node-Current : i
Left Child: 2i + 1 
Right Child: 2i + 2
Parent: (i - 1) / 2
Using Items Count beacause it starts at 1
current = n
left = 2n
right = 2n + 1
root = n/2 => current/2

We fill heaps in the left to right , top to bottom order.
largest item and smallest item find problems.

We initialize the heap list with a zero to represent the dummy first element, and we are adding 
a dummy element just to start the indexing of data items from 1 since if we start indexing from 
1, accessing of the elements becomes very easy due to the parent-child relationship.

Insertion
The insertion of an item into a min heap works in two steps. First, we add the new element to the 
end of the list (which we understand to be the bottom of the tree), and we increment the size of 
the heap by one. Secondly, after each insertion operation, we need to arrange the new element up 
in the heap tree, to organize all the nodes in such a way that satisfies the heap property.
"""

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def insert(self,data):
        #insert item at the end of the heap'
        self.heap.append(data)
        self.size += 1
        #check if it satisfies the heap property
        self.bubble_up(self.size - 1)
    
    def bubble_up(self,position):
        while(position  > 0):
            root_index = (position - 1) // 2
            current_data = self.heap[position]
            root_data = self.heap[root_index]
            if(current_data < root_data):
                self.heap[position], self.heap[root_index] = self.heap[root_index], self.heap[position]
            position = root_index

    def bubble_down(self,position):
        while(position < self.size):
            current = self.heap[position]
            left_child = (2 * position) + 1
            right_child = (2 * position) + 2
            if(current > left_child):
                pass
            if(current > right_child):
                pass
    
    def delete(self):
        if(self.is_empty()):
            return 'Heap is empty'
        #delete the root and then make the root to be the last element
        self.heap[0] = self.heap[self.size - 1]
        del self.heap[self.size - 1]
        self.size -= 1
        #bubble down
        self.bubble_down(0)

if __name__ == '__main__':
    minheap = MinHeap()
    data = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
    for element in data:
        minheap.insert(element)
    print(minheap.heap)
    minheap.delete()
    print(minheap.heap)