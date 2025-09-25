# https://leetcode.com/problems/maximum-product-subarray/submissions/1782457925/
# 152. Maximum Product Subarray
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        till_right = 1
        till_left = 1
        max_val = nums[0]
        for i in range(0,len(nums)):
            till_left = 1 if till_left == 0 else till_left
            till_right = 1 if  till_right ==0 else till_right
            till_left *= nums[i] #== 0 else till_left * nums[i]
            till_right *= nums[len(nums)-1-i] #== 0 else till_right * nums[len(nums)-1-i]
            max_val = max(max_val,max(till_left,till_right))
            print(max_val)
        return max_val
