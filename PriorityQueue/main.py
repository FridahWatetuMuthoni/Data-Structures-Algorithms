class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0][1]
    
    def insert(self, priority, data):
        self.heap.append((priority, data))
        self.size += 1
        self.bubble_up(self.size - 1)
    
    def delete(self):
        if self.is_empty():
            return None
        
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        
        if self.size > 0:
            self.bubble_down(0)
        return root[1]
    
    def get_parent(self, index):
        parent = (index - 1) // 2
        return parent
    
    def get_left_child(self, index):
        left = (index * 2 ) + 1
        return left
    
    def get_right_child(self, index):
        right = (index * 2) + 2
        return right
    
    def bubble_up(self,index):
        parent = self.get_parent(index)
        
        if index > 0 and self.heap[parent][0] > self.heap[index][0]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.bubble_up(parent)
    
    def bubble_down(self, index):
        priority = index
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        
        if left < self.size and self.heap[left][0] < self.heap[priority][0]:
            priority = left
        if right < self.size and self.heap[right][0] < self.heap[priority][0]:
            priority = right
        
        if index != priority:
            self.heap[index], self.heap[priority] = self.heap[priority], self.heap[index]
            self.bubble_down(priority)
    
    def change_priority(self,data, priority):
        index = -1
        for i, value in enumerate(self.heap):
            if value[1] == data:
                index = i
                break
        if index == -1:
            return None
        
        self.heap[index] = ( priority, data)
        self.bubble_up(index)

pq = PriorityQueue()
pq.insert(3, 'Task 1')
pq.insert(1, 'Task 2')
pq.insert(2, 'Task 3')

print(pq.peek())  # Outputs: 'Task 2' (since it has the highest priority 1)

print(pq.delete())  # Outputs: 'Task 2'
print(pq.delete())  # Outputs: 'Task 3'
