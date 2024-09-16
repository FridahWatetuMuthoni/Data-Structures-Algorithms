#BubbleSort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [11, 9, 29, 7, 2, 15, 28]
print(bubble_sort(arr))

#SelectionSort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j  in range(i+1, len(arr)):
            if(arr[j] < arr[min_index]):
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

arr = [11, 9, 29, 7, 2, 15, 28]
print(selection_sort(arr))


#InsertionSort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while(j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j +1] = key
    return arr

arr = [11, 9, 29, 7, 2, 15, 28]
print(insertion_sort(arr))

#QuickSort
def quick_sort(arr):
    if(len(arr) <= 1):
        return arr
    
    last_index = len(arr) - 1
    pivot = arr[last_index]
    i = 0
    j = last_index - 1
    
    while(i <= j):
        if(arr[i] <= pivot):
            i += 1
        else:
            if(arr[j] <= pivot):
                arr[i], arr[j] = arr[j],arr[i]
            j -= 1
    arr[i], arr[last_index] = arr[last_index], arr[i]
    
    right_array = quick_sort(arr[0:i])
    left_array = quick_sort(arr[i+1:])
    
    return right_array + [arr[i]] + left_array


arr = [11, 9, 29, 7, 2, 15, 28]
print(quick_sort(arr))

#MergeSort
def merge_sort(arr):
    if(len(arr) <= 1):
        return arr
    
    #slipt arr
    left, right = split_array(arr)
    left_array = merge_sort(left)
    right_array = merge_sort(right)
    
    #combine them
    return merge(left_array, right_array)

def split_array(arr):
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]
    return left, right

def merge(left, right):
    i = 0
    j = 0
    sorted_array = []
    
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
            
    if(i < len(left)):
        sorted_array += left[i:]
        
    if(j < len(right)):
        sorted_array += right[j:]
    return sorted_array

arr = [11, 9, 29, 7, 2, 15, 28]
print(merge_sort(arr))