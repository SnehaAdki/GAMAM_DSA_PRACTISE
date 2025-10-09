# https://leetcode.com/problems/longest-consecutive-sequence/submissions/1796457156/
# 128. Longest Consecutive Sequence
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3


def longestConsecutive(nums):
    nums.sort()
    curr_con = max_con = 1
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1] == 1:
            curr_con += 1
        elif nums[i]-nums[i-1] > 1:
            max_con = max(max_con, curr_con)
            curr_con = 1
    print(max(max_con, curr_con))
            
       

nums = [100,6,200,7,3,2]
longestConsecutive(nums)
