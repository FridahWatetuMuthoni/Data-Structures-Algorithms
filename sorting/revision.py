#Bubble Sort

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [10,20,80,16,2,5,30]
print(bubble_sort(arr))

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

arr1 = [10,20,80,16,2,5,30]
print(selection_sort(arr1))


def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        
        while( j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    return arr

arr2 = [10,20,80,16,2,5,30]
print(insertion_sort(arr2))


def merge_sort(arr):
    if(len(arr) <= 1):
        return arr
    
    #continously split the list
    left, right = split_list(arr)
    left_array = merge_sort(left)
    right_array = merge_sort(right)
    
    return merge(left_array, right_array)

def split_list(arr):
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]
    return left, right

def merge(left, right):
    sorted_array = []
    i = 0
    j = 0
    
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    if(i < len(left)):
        sorted_array += left[i:]
    if(j <len(right)):
        sorted_array += right[j:]
    return sorted_array

arr3 = [30,900,700,800,20,70,80]
print(merge_sort(arr3))