"""
How it works:
1. set the first element as minimum
2. Compare minimum with the second elemet. if the second element is smaller than minimum,
assign the second element as minimum... do this untill the end.
3. After each iteration, minimum is place at the front of the sorted list
4. for each iteration, indexing starts from the first unsorted element
"""

def selection_sort(arr):
    #loop thru the array
    for i in range(len(arr)):
        #assume the first element of the array is the minimum
        min_index = i
        #find the minimum element in the remaining usorted part
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min_index]):
                min_index = j
        # Swap the found minimum element with the element at index 'i'
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [21,38,29,17,4,25,11,32,9]
print(selection_sort(arr))




def selection(arr):
    #loop thru the array
    for i in range(len(arr)):
        #set the minimum value as first element in the current unsorted array
        min = i
        #loop thru the unsorted array to find the smallest value
        for j in range(i+1, len(arr)):
            if(arr[min] > arr[j]):
                min = j
        #swap
        arr[min], arr[i] = arr[i], arr[min]
        
    return arr

arr = [21,38,29,17,4,25,11,32,9]
print(selection(arr))

