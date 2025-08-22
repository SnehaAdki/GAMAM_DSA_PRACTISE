# DP
# https://leetcode.com/problems/trapping-rain-water/description/
# 42. Trapping Rain Water (Total Water trapping)
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Given n non-negative integers representing an elevation map where
# the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

def container(nums):
    total_area = 0
    left = 0
    right = len(nums)-1
    l_max = 0
    r_max = 0

    while left < right:
        l_max = max(l_max , nums[left])
        r_max = max(r_max,nums[right])

        if l_max < r_max:
            total_area += l_max - nums[left]
            left+=1
        else:
            total_area += r_max-nums[right]
            right-=1

    return total_area



height = [4,2,8,3,2,5]
print(container(height))
