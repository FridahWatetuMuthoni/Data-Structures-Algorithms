"""
How it works:
1. choose a pivot element (usually last or random)
2. Store elements less than pivot in left subarray
3. Store elements greater than pivot in the right subarray
4. call quicksort recursively on left subarray
5. call quicksort recursively on the right subarray

"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    last_index = len(arr) - 1
    pivot = arr[last_index]
    i = 0
    j = last_index - 1
    
    while( i <= j):
        if(arr[i] <= pivot):
            i += 1
        else:
            if(arr[j] <= pivot):
                arr[j], arr[i] = arr[i],arr[j]
            j -= 1
    
    arr[i], arr[last_index] = arr[last_index],arr[i]
    
    left_sorted = quick_sort(arr[0:i])
    right_sorted = quick_sort(arr[i+1:])
    
    return left_sorted + [arr[i]] + right_sorted

arr = [11, 9, 29, 7, 2, 15, 28]
print(quick_sort(arr))


def quickSort(arr):
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
                arr[j], arr[i] = arr[i],arr[j]
            j -= 1
            
    arr[last_index], arr[i] = arr[i],arr[last_index]
    
    right_array = quickSort(arr[0:i])
    left_array = quickSort(arr[i+1:])
    
    return right_array + [arr[i]] + left_array



arr2 = [8,2,4,7,1,3,9,6,5]
print(quickSort(arr2))
