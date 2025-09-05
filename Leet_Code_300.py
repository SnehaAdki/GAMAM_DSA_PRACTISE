# DP
# Leet Code 300
# https://leetcode.com/problems/longest-increasing-subsequence/submissions/1760515810/

# 300. Longest Increasing Subsequence
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return the length of the longest strictly increasing subsequence.


# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4 

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1


def find_lar_sub(arr):
    temp = [1] * len(arr)
    
    i=1
    j=0
    while i < len(arr):
        while j != i:
            if arr[i] > arr[j]:
                if temp[i] < temp[j]+1:
                    temp[i]+=1
            j += 1
        if j == j:
            j =0 
        i+=1

    return max(temp)


arr= [0,1,0,3,2,3]
print(find_lar_sub(arr))
