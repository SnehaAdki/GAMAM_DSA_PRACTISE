# 189. Rotate Array
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


def rotate(arr,k):
    for i in range(k):
        temp_last = arr[-1]
        for j in range(len(arr)-1,0,-1):
            arr[j] = arr[j-1]
        arr[0] = temp_last

    print(arr)

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums,k)


# optiomal

class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k %len(arr)
        arr.reverse()
        arr[0:k] = arr[0:k][::-1]
        arr[k:len(arr)] = arr[k:len(arr)][::-1]
