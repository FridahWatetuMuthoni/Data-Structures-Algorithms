class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def insert_at_tail(self,data):
        new_node = Node(data)
        if(self.is_empty()):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def insert_at_head(self,data):
        new_node = Node(data)
        if(self.is_empty()):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    
    def insert_at_index(self,data, index):
        if(index < 0 or index > self.size):
            return 'index is out of bounds'
        if(index == 0):
            return self.insert_at_head(data)
        if(index == self.size):
            return self.insert_at_tail(data)
        
        new_node = Node(data)
        
        if(self.is_empty()):
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            count = 0
            while(current != None):
                if(count == index - 1):
                    break
                else:
                    current = current.next
                    count += 1
            next = current.next
            current.next = new_node
            new_node.next = next
        self.size += 1
    
    def delete(self,index):
        if(self.is_empty()):
            return 'The list is empty'
        if(index < 0 or index > self.size ):
            return 'The index is out of bound'
        
        if(self.head == self.tail):
            current = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return current.data
        
        if(index == 0):
            #remove at head
            removed_data = self.head.data
            next = self.head.next
            self.head = next
            self.size -= 1
            return removed_data
        else:
            #remove at index
            count = 0
            prev = None
            current = self.head
            while(current != None):
                if(count == index):
                    removed_data = current.data
                    next = current.next
                    prev.next = next
                    if(current == self.tail):
                        self.tail = prev
                    self.size -= 1
                    return removed_data
                prev = current
                current = current.next
                count += 1
    
    def search(self,data):
        current = self.head
        count = 0
        
        while(current != None):
            if(current.data == data):
                return count
            current = current.next
            count += 1
        return None
    
    def print_list(self):
        str = ""
        current = self.head
        while(current != None):
            if(current == self.head and current == self.tail):
                str += f"[{current.data}]"
            elif(current == self.head):
                str += f"[Head:{current.data}]=>"
            elif(current == self.tail):
                str += f"[{current.data}:Tail]"
            else:
                str += f"{current.data}=>"
            current = current.next
        print(str)
        return str

ll = LinkedList()
ll.insert_at_head(20)
ll.insert_at_head(30)
ll.insert_at_head(40)
ll.insert_at_tail(70)
ll.insert_at_tail(80)
ll.insert_at_tail(90)
ll.insert_at_index(700,2)
ll.insert_at_index(800,3)
ll.insert_at_index(900,2)
ll.insert_at_index(1000,3)
ll.print_list()
ll.delete(3)
ll.print_list()
ll.delete(0)
ll.print_list()
ll.delete(ll.size - 1)
ll.print_list()