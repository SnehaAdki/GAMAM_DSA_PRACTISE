# DP
# https://leetcode.com/problems/trapping-rain-water/description/
# 42. Trapping Rain Water
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

def container(nums):
    max_area = 0
    curr_area = 0
    left = 0
    right = len(nums)-1

    while left < right:
        curr_area = min(nums[left],nums[right])* (right-left)
        if nums[left]<nums[right]:
            left+=1
        else:
            right-=1
        max_area = max(curr_area,max_area)
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(container(height))
