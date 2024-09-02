class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.size == 0
    
    def insert_at_begining(self, data):
        new_node = Node(data)
        
        if(self.is_empty()):
            self.head = new_node
            self.tail = new_node
        else:
            next = self.head
            new_node.next = next
            self.head = new_node
        self.size += 1
    
    def insert_at_end(self,data):
        new_node = Node(data)
        
        if(self.is_empty()):
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            current.next = new_node
            self.tail = new_node
        self.size += 1
    
    def insert_at_index(self,index,data):
        new_node = Node(data)
        current_index = 0
        current = self.head
        prev = None
        
        if(index < 0 or index > self.size):
            return 'index is out of bound'
        
        if(index == 0):
            return self.insert_at_begining(data)
        
        if(index == self.size):
            return self.insert_at_end(data)
        
        while(current_index < index):
            prev = current
            current_index += 1
            current = current.next
        
        prev.next = new_node
        new_node.next = current
        self.size += 1
    
    def delete_at_index(self,index):
        print(f"index:{index}")
        if(index < 0 or index > self.size):
            return 'index is out of bound'
        
        if(index == 0):
            value = self.head.data
            next = self.head.next
            self.head = next
            return value
        
        current = self.head
        current_index = 0
        prev = None
        while(current != None):
            if(index == current_index):
                if(current == self.tail):
                    value = current.data
                    prev.next = None
                    self.tail = prev
                    return value
                else:
                    value = current.data
                    next = current.next
                    prev.next = next
                    return value
            prev = current
            current = current.next
            current_index+=1
        

        self.size -= 1
    
    def find_at_index(self,index):
        if(index < 0 or index > self.size):
            return 'index is out of bound'
        
        if(index == 0):
            return self.head.data
        
        if(index == self.size - 1):
            return self.tail.data
        
        current = self.head
        current_index = 0
        while(current != None):
            if(current_index == index):
                return current.data
            current = current.next
            current_index+=1
    
    def display_list(self):
        current  =  self.head
        str = ""
        
        if(self.head == self.tail):
            return f'Single Node: {self.head.data}'
        
        while(current != None):
            if(current == self.head):
                str += f"[Head:{current.data}]=>"
            elif(current == self.tail):
                str += f"[Tail:{current.data}]"
            else:
                str += f"{current.data}=>"
            current = current.next
        return str

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_begining(10)
    l1.insert_at_begining(20)
    l1.insert_at_begining(30)
    l1.insert_at_begining(40)
    l1.insert_at_end(60)
    l1.insert_at_end(70)
    l1.insert_at_end(80)
    l1.insert_at_index(2,100)
    l1.insert_at_index(0,700)
    l1.insert_at_index(l1.size,900)
    print(l1.find_at_index(3))
    print(l1.display_list())
    print(l1.delete_at_index(l1.size-1))
    print(l1.display_list())