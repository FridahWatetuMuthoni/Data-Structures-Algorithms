"""
For an array we need to find the max sum of p consecutive elements
"""


"""
Minimum subarray sum => 209:
Given an array of positive intergers nums and a positive integer target, return the minimal length of a sub array whose
sum is greater than or equal to target. If none found return 0
"""

def minSubArray(target, numbers):
    start = 0
    end = 0
    

arr1 = [2,3,1,2,4,3]
tag1 = 7
#2

arr2 = [1,4,4]
tag2 = 4
#1

arr3 = [1, 1, 1, 1, 1, 1, 1, 1]
tag3 = 11
#0