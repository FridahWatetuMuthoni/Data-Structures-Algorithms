"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order
Binary Heap => values are added left to right
min => the minimum value is always at the top
max => the maximum value is always at the top
insert => bubble up
remove => bubble down
"""

def most_frequent_elements(nums, k):
    seen = set()

nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(most_frequent_elements(nums1,k1))
#output = [1, 2]

nums2 = [1]
k2 = 1
#output = [1]
print(most_frequent_elements(nums2,k2))
