# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Leet Code 34
# 34. Find First and Last Position of Element in Sorted Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums, target):
        left = self.get_left(nums,target)
        right = self.get_right(nums,target)

        return[left , right]

    def get_left(self,nums,target):
        index = -1
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high) //2
            if nums[mid] == target:
                index = mid
                high = mid -1
            elif nums[mid] < target:
                low = mid +1
            else:
                high = mid-1
        return index

    def get_right(self,nums,target):
        index = -1
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high) //2
            if nums[mid] == target:
                index = mid
                low = mid +1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return index
