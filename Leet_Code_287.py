# DP
# https://leetcode.com/problems/find-the-duplicate-number/
# Leet Code 287. 
# Find the Duplicate Number
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:
# Input: nums = [3,3,3,3,3]
# Output: 3

def findDuplicate(nums):
    hash_map = {}
    for i in nums:
        if i in hash_map:
            return i
        hash_map[i] = 1


nums = [1,3,4,2,2]
print(findDuplicate(nums))
  
