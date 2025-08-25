# DP
# Leet_code_56
# 56. Merge Intervals
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge(intervals):
    intervals.sort()
    print(intervals)
    final = []
    final.append(intervals[0].copy())
    i = 1
    while i < len(intervals):
        if final[-1][-1] >= intervals[i][0]:
            final[-1][-1] = max(intervals[i][-1],final[-1][-1])
        elif final[-1][-1] < intervals[i][0]:
            final.append(intervals[i].copy())
        i+=1
    return final

intervals = [[1,4],[2,3]]

print(merge(intervals))
# intervals = [[0, 4], [1, 5]]
# print(merge(intervals))
