arr = [21,38,29,17,4,25,11,32,9]

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j +1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j+1]
    return arr


print(bubbleSort(arr[:]))

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

print(selectionSort(arr[:]))

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > key):
            arr[j +1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print(insertionSort(arr[:]))

def quick_sort(arr):
    #base case
    if len(arr) <= 1:
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
                arr[j], arr[i] = arr[i], arr[j]
            j -= 1
    arr[i],arr[last_index]= arr[last_index],arr[i]
    
    left_array = quick_sort(arr[0:i])
    right_array = quick_sort(arr[i+1:])
    
    return left_array + [arr[i]] + right_array

print(quick_sort(arr[:]))

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    #split the array
    left,right = split_array(arr)
    
    #call merge sort on both arrays
    left_array = mergeSort(left)
    right_array = mergeSort(right)
    
    #merge and return the arr
    return merge(left_array, right_array)

def split_array(arr):
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]
    return left, right

def merge(left,right):
    i  = 0
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
    if( j < len(right)):
        sorted_array += right[j:]
    return sorted_array

print(mergeSort(arr[:]))
