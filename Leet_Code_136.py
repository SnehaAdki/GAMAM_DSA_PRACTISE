# Leet Code 136
# https://leetcode.com/problems/single-number/submissions/1825975957/

# 136. Single Number

# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1


def singleNumber(nums):
    hash_map = {}
    hash_res = []
    res = 0
    # for i in nums:
    #     if hash_map.get(i):
    #         hash_map[i] += hash_map[i]
    #     else:
    #         hash_map[i] = 1
    
    # for i in hash_map.keys():
    #     if hash_map[i] == 1:
    #         res = i
    # print(hash_map)
    # print(res)
    for i in range(0,len(nums)):
        if nums[i] in hash_res:
            hash_res.remove(nums[i])
        else:
            hash_res.append(nums[i])

    print(hash_res[0])
            


nums = [4,2,1,2,1]
singleNumber(nums)
