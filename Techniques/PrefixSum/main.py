"""
find the sum of the numbers in the given index range (14,29)
pref[i] = pref[i-1] + a[i-1]
"""

#O(n)
def sum_in_range_brute_force(start, end):
    total = 0
    while(start < end):
        print(start)
        total += start
        start+=1
    return total

print(sum_in_range_brute_force(14,29))


def sum_in_range(arr):
    total = 0
    
    sums = [0] * (len(arr) + 1) #plus one because the start is going to be zero
    
    #Generate prefix sum array
    for index in range(len(numbers)):
        sums[index + 1] = sums[index] + numbers[index]
    
    #finding sum of numbers in give index range
    rangeSum = sums[29] - sums[14]
    print(rangeSum)


numbers = [2,8,9,11,12,26,27,29,33,36,37,42,44,46,47,52,56,57,58,60,61,64,68,70,72,73,76,77,78,80,82,83,95,96,98,99]
sum_in_range(numbers)