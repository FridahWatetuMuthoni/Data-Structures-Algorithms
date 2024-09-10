"""
Things to consider when choosing pointers:
1. The physical significance of the pointer e.g the range(i, j), pairs.
2. How to initialize the pointers: range(start, end), pair(first element and second element), first three elements.
3. How to move the pointers
4. When to stop
"""

""" 
Give a sorted array, find the number of pairs which their sum is k
"""
def sum_of(arr, target):
    result = []
    start = 0
    end = len(arr) - 1
    
    while(start < end):
        sum = arr[start] + arr[end]
        
        if(sum == target):
            result.append([arr[start], arr[end]])
        
        if(sum < target):
            start += 1
        else:
            end -= 1
    return result


arr = [1,2,3,4,5,6,7,8,9,10]
target = 11
print(sum_of(arr, target))
