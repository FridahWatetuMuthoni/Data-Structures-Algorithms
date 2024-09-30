class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        self.bubble_up(self.size - 1)
    
    def delete(self):
        if self.is_empty():
            return 'Empty'
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        
        if self.size > 0:
            self.bubble_down(0)
            
        return root
    
    def bubble_down(self, index):
        smallest = index
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        
        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.bubble_down(smallest)
    
    def bubble_up(self, index):
        parent = self.get_parent(index)
        
        if parent >= 0 and self.heap[parent] > self.heap[index]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.bubble_up(parent)
    
    def get_parent(self,index):
        parent = (index - 1) // 2
        return parent
    
    def get_left_child(self, index):
        left = (2 * index) + 1
        return left
    
    def get_right_child(self, index):
        right = (2 * index) + 2
        return right
    
    def heap_sort(self):
        original_size = self.size
        original_heap = self.heap[:]
        results = []
        
        for _ in range(self.size):
            results.append(self.delete())
        
        self.size = original_size
        self.heap = original_heap
        return results

# Create a new MinHeap instance
min_heap = MinHeap()

# Insert elements
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(5)
min_heap.insert(15)
min_heap.insert(1)

# After these insertions, the heap should follow the min-heap property.
print(min_heap.heap)