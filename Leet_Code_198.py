# DP
# Leet Code 198
# https://leetcode.com/problems/house-robber/submissions/1752486251/
# 198. House Robber
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

def rob(num):
    odd_sum = 0
    odd_even = 0
    for i in range(0,len(num),+2):
        odd_sum+=num[i]
    for i in range(1,len(num),+2):
        odd_even+=num[i]

    print(odd_even,odd_sum)
    return odd_sum if odd_sum > odd_even else odd_even


def rob_optimal(nums):
    max_arr = []
    max_arr.append(nums[0])
    for i in range(1,len(nums)):
        if i == 1:
            max_arr.append(max(nums[i],max_arr[-1]))
        else:
            max_arr.append(max(max_arr[i-2]+nums[i],max_arr[i-1]))
        
    return max_arr[-1]

nums=[1,2,3,1]
print(rob_optimal(nums))
