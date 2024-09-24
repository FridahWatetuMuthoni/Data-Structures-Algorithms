def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

arr1 = [21,38,29,17,4,25,11,32,9]
print(bubble_sort(arr1))

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

arr2 = [21,38,29,17,4,25,11,32,9]
print(selection_sort(arr2))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while(j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr3 = [21,38,29,17,4,25,11,32,9]
print(selection_sort(arr3))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    last_index = len(arr) - 1
    pivot = arr[last_index]
    i = 0
    j = last_index - 1
    
    while(i <= j):
        if arr[i] < pivot:
            i += 1
        else:
            if arr[j] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
            j -= 1
    arr[i], arr[last_index] = arr[last_index], arr[i]
    
    left_arr = quick_sort(arr[0:i])
    right_arr = quick_sort(arr[i+1:])
    
    return left_arr + [arr[i]] + right_arr

arr4 = [21,38,29,17,4,25,11,32,9]
print(quick_sort(arr4))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    #split the arr
    left, right = split_array(arr)
    
    left_array = merge_sort(left)
    right_array = merge_sort(right)
    
    return merge(left_array, right_array)

def split_array(arr):
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]
    return left, right

def merge(left,right):
    i = 0
    j = 0
    sorted_arr = []
    
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    if i < len(left):
        sorted_arr += left[i:]
    if j < len(right):
        sorted_arr += right[j:]
    return sorted_arr
            
arr5 = [21,38,29,17,4,25,11,32,9]
print(merge_sort(arr5))
