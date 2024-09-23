"""
Binary Heaps Properties:
Binary heaps must be filled left to right.
Every parent must be greater than its children nodes for a max heap
Every parent must be less than its children nodes for a min heap
parent index = (i - 1) // 2
left child = 2i + 1 
right child = 2i + 2
"""

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = len(self.heap)
    
    def is_empty(self):
        return self.size == 0
    
    def insert(self,data):
        self.heap.append(data)
        self.bubble_up(self.size - 1)
        return data
    
    def delete(self):
        if self.is_empty():
            return 'The heap is empty'
        current = self.heap[0]
        self.heap[0]= self.heap[-1]
        self.heap.pop()
        
        #first check if the heap is empty after delete before calling bubble down
        if not self.is_empty():
            self.bubble_down(0)
        return current
    
    def peek(self):
        if self.is_empty():
            return 'Heap is empty'
        return self.heap[0]
    
    def bubble_up(self,index):
        parent = self.get_parent(index)
        
        if index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.bubble_up(parent)
    
    def bubble_down(self,index):
        smallest = index
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        
        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[smallest],self.heap[index] = self.heap[index], self.heap[smallest]
            self.bubble_down(smallest)
    
    def get_parent(self,index):
        parent = (index - 1) // 2
        return parent
    
    def get_left_child(self,index):
        left = (index * 2) + 1
        return left
    
    def get_right_child(self,index):
        right = (index * 2) + 2
        return right
    
    def heap_sort(self):
        sorted_arr = []
        original_size = self.size
        for _ in range(original_size):
            sorted_arr.append(self.delete())
        return sorted_arr