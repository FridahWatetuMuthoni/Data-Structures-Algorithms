class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.is_empty():
            return 'The heap is empty'
        return self.heap[0]
    
    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        self.bubble_up(self.size - 1)
    
    def delete(self):
        if self.is_empty():
            return 'heap is empty'
        
        current = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        
        if not self.is_empty():
            self.bubble_down(0)
        return current
    
    def get_parent(self, index):
        parent = (index - 1) // 2
        return parent
    
    def get_left_child(self, index):
        left = (2 * index) + 1
        return left
    
    def get_right_child(self, index):
        right = (2 * index) + 2
        return right
    
    def bubble_up(self, index):
        parent = self.get_parent(index)
        
        if index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.bubble_up(parent)
    
    def bubble_down(self,index):
        largest = index
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        
        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.bubble_down(largest)
    
    def heap_sort(self):
        sorted_array = []
        
        original_size = self.size
        original_heap = self.heap.copy()
        
        for _ in range(self.size):
            sorted_array.insert(0, self.delete())
        
        self.size = original_size
        self.heap = original_heap
        return sorted_array
    