"""
How it works
1. loop thru the elements n-1 times while comparing arr[i] and arr[i+1]
2   if arr[i] > arr[i+1] => swapp them
2. Reapeat the process (n-1-i) times
3. check if the list is swapped to avoid unneccessary looping

"""

def bubbleSort(arr):
    size = len(arr)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 -i):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
arr = [38,9,29,7,2,15,28]
print(bubbleSort(arr))

arr2 = ["mona","dhaval","aamir","tina","chang"]
print(bubbleSort(arr2))



def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for i in range(len(arr) - 1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print('sorting')
                swapped = True
        if not swapped:
            print('sorted')
            break
    return arr

arr3 = [21,38,29,17,4,25,11,32,9]
print(bubble_sort(arr3))
