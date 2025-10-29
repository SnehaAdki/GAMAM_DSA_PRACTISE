# Leet Code 78
# https://leetcode.com/problems/subsets/submissions/1815193560/
# 78. Subsets
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.



# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]



def subsets_array(nums):
    final = []
    temp_list =[]
    print(final)

    def backtrack(index):
        if index >= len(nums):
            final.append(temp_list.copy())
            return
        
        temp_list.append(nums[index])
        backtrack(index+1)
        
        temp_list.pop()
        backtrack(index+1)
    backtrack(0)
    return final

    
nums = [1,2,3]
subsets_array(nums)
