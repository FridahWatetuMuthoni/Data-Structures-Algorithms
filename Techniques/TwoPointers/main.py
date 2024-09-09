def palindrome(str):
    start = 0
    end = len(str)-1
    
    while(start < end):
        if(str[start] != str[end]):
            return False
        start += 1
        end -= 1
    return True

print(palindrome('anna'))
print(palindrome('racecar'))
print(palindrome('freecodecamp'))
print(palindrome('fridah'))

#O(n)
def two_sum(arr, target):
    start = 0
    end = len(arr) - 1
    
    while(start < end):
        sum = arr[start] + arr[end]
        
        if(sum == target):
            return [arr[start], arr[end]]
        
        if(sum < target):
            start += 1
        else:
            end -= 1

arr = [3,2,4]
target = 6
print("Two sum")
print(two_sum(arr, target))

#O(n)
def two_sum_unsorted(arr, target):
    seen = {}
    
    for i, value in enumerate(arr):
        compliment = target - value
        if(compliment in seen):
            return [compliment, value]
        else:
            print(seen)
            seen[value] = i
    return None

arry = [3, 5, 2, -4, 8, 11]
total = 19
print(two_sum_unsorted(arry,total))


def reverse_string(str):
    letters = []
    reversed_string = []
    
    for letter in str:
        letters.append(letter)
    
    while(len(letters) > 0):
        reversed_string.append(letters.pop())
    
    return "".join(reversed_string)
    

print(reverse_string('fridah'))


"""
The "move zeros" problem involves moving all the 0s in an array to the end while maintaining the relative order
of the non-zero elements. You can solve this efficiently using the two-pointer technique.

"""
def move_zeros(arr):
    non_zero_position = 0
    
    for index, value in enumerate(arr):
        if value != 0:
            arr[index],arr[non_zero_position] =arr[non_zero_position], arr[index]
            non_zero_position += 1
    return arr

arr = [0, 1, 0, 3, 12]
print(move_zeros(arr)) #[1,3,12,0,0]


def has_cycle(head):
    if not head and not head.next:
        return False
    
    fast_pointer = head
    slow_pointer = head
    
    while(slow_pointer != None and fast_pointer.next != None):
        #move the pointers
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        #check for cycles
        if(slow_pointer == fast_pointer):
            return True
    return False