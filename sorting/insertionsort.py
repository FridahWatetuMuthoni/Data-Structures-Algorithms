"""
How it works:
1. 
"""

def insertion_sort(arr):
    #start from the second element
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        
        while(j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [40,21,38,29,17,4,25,11,32,9]
print(insertion_sort(arr))



def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while(j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr2 = [6,1,7,4,2,9,8,5,3]
print(insertionSort(arr2))