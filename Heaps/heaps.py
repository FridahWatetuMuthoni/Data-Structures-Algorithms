"""
Binary Heap Properties.
1. The heap property: The heap is filled left to right , top to bottom. Each node should be smaller or equal to its children for a min heap
and each node should be greater or equal to its children in a max heap.
2. Each parent node can have at most two children

Access Items in a Binary Heap:
n = i
left_child = 2i + 1
right_child = 2i + 2
parent = (i - 1) // 2

Min Heap === priority queue
"""

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def insert(self,data):
        #add element at the end of the array/heap
        self.heap.append(data)
        self.size += 1
        
        self.bubble_up(self.size - 1)
    
    def remove(self):
        if (self.is_empty()):
            return 'The heap is empty'
        #get the root value
        root_data = self.heap[0]
        #put the last element at the start
        self.heap[0] = self.heap[self.size - 1]
        #delete the last element
        self.heap.pop()
        self.size -= 1
        #bubble everything down to satisfy the heap property
        if not self.is_empty():
            self.bubble_down(0)
        return root_data

    
    def bubble_up(self, index):        
        while(index > 0):
            parent_index = self.get_root(index)
            #compare the root and the current data 
            if(self.heap[index] < self.heap[parent_index]):
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    
    def bubble_down(self, index):
        while True:
            smallest = index
            left_index = self.get_left_index(index)
            right_index = self.get_right_index(index)
            
            #find the smallest between left and right value and if the indexes are valid
            if(left_index < self.size and self.heap[left_index] < self.heap[smallest]):
                smallest = left_index
            
            if(right_index < self.size and self.heap[right_index] < self.heap[smallest] ):
                smallest = right_index
            
            if(smallest == index):
                break
            
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            index = smallest
            
        
    
    def get_root(self,index):
        root = (index - 1) // 2
        return root
    
    def get_left_index(self,index):
        left = (2 * index) + 1
        return left
    
    def get_right_index(self,index):
        right = (index * 2 ) + 2
        return right
    
    #O(n log n)
    def heapify(self, arr):
        if(len(arr) > 0):
            for element in arr:
                self.insert(element)
        return self.heap
    
    #O(n)
    def heapify_two(self, arr):
        self.heap = arr[:]
        self.size = len(arr)
        for i in range(self.size // 2, -1, -1):
            self.bubble_down(i)
        return self.heap
    
    def heap_sort(self):
        sorted_heap = []
        while(self.size > 0):
            #smallest element
            smallest = self.heap[0]
            #put the last element at first index and then pop it
            self.heap[0] = self.heap[self.size -1]
            self.heap.pop()
            self.size -= 1
            self.bubble_down(0)
            sorted_heap.append(smallest)
        return self.sorted_heap
        