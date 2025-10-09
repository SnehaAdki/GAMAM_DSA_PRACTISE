# https://leetcode.com/problems/permutations/submissions/1796515700/

# Leet Code 46. Permutations
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]



class Solution:
    def permute(self, nums):
        
        all_per = []

        def back_track(all_per,cur,nums):
            if len(cur) == len(nums):
                all_per.append(cur[:])
                return
            
            for i in range(0,len(nums)):
                if nums[i] in cur:
                    continue
                
                cur.append(nums[i])
                back_track(all_per,cur,nums)
                cur.pop()

        back_track(all_per, [] , nums)
        return all_per
