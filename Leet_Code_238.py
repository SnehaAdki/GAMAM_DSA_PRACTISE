# DP
# Leet Code 238
# https://leetcode.com/problems/product-of-array-except-self/submissions/1752394837/
# 238. Product of Array Except Self
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Brute Force
def product_apart_itself(nums):
    final = []
    for i in range(0,len(nums)):
        prd = 1
        for j in range(0,len(nums)):
            if nums[i] != nums[j]:
                prd *=nums[j]

        final.append(prd)
    return final


# Optimal Solution
def product_apart_itself_optimal(nums):
    left = []
    left.append(1)
    for i in range(1,len(nums)):
        left.append(nums[i-1]*left[-1])

    right = []
    right.append(1)
    for i in range(len(nums)-2,-1,-1):
        right.append(nums[i+1]*right[-1])
    
    right = right[::-1]
    final_arr =[]
    for i in range(0,len(nums)):
        final_arr.append(left[i]*right[i])
    

    return final_arr



nums = [3,4,6,1,2]
# nums = [-1,1,0,-3,3]
print(product_apart_itself_optimal(nums))
