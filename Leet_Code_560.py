# Leet Code 560
# http://leetcode.com/problems/subarray-sum-equals-k/description/
# 560. Subarray Sum Equals K
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2


# brute Force Approac
def rtn_sum_brute(nums,k):
    count = 0 
    for i  in range(len(nums)):
        sum = 0 
        for j in range(i,len(nums)):
            sum += nums[j]
            if k == sum:
                count+=1
    print(count)


def rtn_sum_optimal(nums,k):
    pre_sum = []
    sum = 0
    for i in nums:
        sum +=i
        pre_sum.append(sum)

    hash_map = {}
    count = 0

    for j in range(len(nums)):
        if(pre_sum[j] == k):
            count+=1

        if (pre_sum[j]-k) in hash_map:
            count+=hash_map[pre_sum[j]-k]
            
        if pre_sum[j] not in hash_map.keys():
            hash_map[pre_sum[j]] = 1
        else:
            hash_map[pre_sum[j]]+=1
        
    print(count)




# nums = [9,4,0,20,3,10,5]
# k = 33
nums = [1,-1,0]
k  =0 
#rtn_sum_brute(nums,k)
rtn_sum_optimal(nums,k)
