"""
Recursion
A recursive algorithm calls itself repeatedly in order to solve the problem until a certain condition 
is fulfilled. Each recursive call itself spins off other recursive calls. A recursive function can be in 
an infinite loop; therefore, it is required that each recursive function adheres to certain properties. 
At the core of a recursive function are two types of cases:
1. Base cases: These tell the recursion when to terminate, meaning the recursion will be 
stopped once the base condition is met.
2. Recursive cases: The function calls itself recursively, and we progress toward achieving 
the base criteria.
"""

def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n-1)
print(factorial(5))


def sum(n):
    if(n == 0):
        return 0
    return n + sum(n-1)
print(sum(5))

def binary_search_iteration(arr, element):
    start = 0
    end = len(arr)
    while(start < end):
        print(arr[start:end])
        mid = (start + end) // 2
        if(arr[mid] == element):
            return True
        elif(arr[mid] > element):
            end = mid
        else:
            start = mid
    return False

def binary_search_recursion(arr, element, start, end):
    if(start > end):
        return False
    mid  = (start + end ) // 2
    if(arr[mid] == element):
        return True
    elif(arr[mid] > element):
        return binary_search_recursion(arr, element, 0, mid-1)
    else:
        return binary_search_recursion(arr, element, mid+1, end)

arr = [2,4,7,9,11,13,15,16,20,24, 26,29, 32, 35, 38,39,40,61,66,70,78,80,90,95]
print(binary_search_recursion(arr,95, 0, len(arr)-1))


lookup = {}
def fibonacci(number):
    if number in lookup:
        return lookup[number]
    if number == 0:
        return 0
    elif number == 1:
        return 1
    
    else:
        value = fibonacci(number-1) + fibonacci(number-2)
        lookup[number] = value
        return value
# Print the first 11 Fibonacci numbers
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
