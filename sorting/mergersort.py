def merge_sort(arr):
    """
    merge_sorts sorts a list in ascending order
    """
    # countinously divide the list into smaller list : divided by two with mid point
    # recursively sort the sublists created in previous step
    # combine: merger the sorted sublists created from previous step
    
    #the base condition
    if(len(arr) <= 1):
        return arr
    
    #divide the arr into sublists
    left_half, right_half = split_list(arr)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split_list(arr):
    mid = len(arr) // 2
    left_half = arr[0:mid]
    right_half = arr[mid:]
    return left_half, right_half

def merge(left, right):
    i = 0
    j = 0
    sorted_arr = []
    
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    if(i < len(left)):
        sorted_arr += left[i:]
    if(j < len(right)):
        sorted_arr += right[j:]
    return sorted_arr

arr = [8, 4, 5, 1,3,2,6,7]
print(merge_sort(arr))