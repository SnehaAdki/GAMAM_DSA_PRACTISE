# https://leetcode.com/problems/majority-element/submissions/1816885777/
# Leet Code 169
# 169. Majority Element
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


def majority_elements(nums):
    max_ele = len(nums) // 2
    hash_map = {}
    
    for i in nums:
       hash_map[i]=hash_map.get(i,0)+1
       if hash_map[i] > max_ele:
           return i
    
    
    
    print(hash_map)

nums = [2,2,1,1,1,2,2]
print(majority_elements(nums))
