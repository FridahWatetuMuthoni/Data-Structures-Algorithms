
def binary_search_inter(arr,target):
    start = 0
    end = len(arr) - 1
    
    while(start <= end):
        mid = (start + end) // 2
        
        if(arr[mid] == target):
            return mid
        elif(arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return None

arr = [2,3,4,6,15,17,19,20]
print(binary_search_inter(arr,19))

def binary_search_recur(arr,target, start, end):
    #if the length of the array is zero and the value has yet to be found return None
    if(start > end):
        return None
    #calculate start, end, mid
    mid = (start + end) // 2 
    
    if(arr[mid] == target):
        return mid
    elif(arr[mid] > target):
        return binary_search_recur(arr, target, start, mid - 1)
    else:
        return binary_search_recur(arr,target, mid+1, end)


arr1 = [2,3,4,6,15,17,19,20]
print(binary_search_recur(arr1,17, 0, len(arr1)-1))