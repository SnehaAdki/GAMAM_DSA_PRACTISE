#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


def twoSum( nums,target):
    hash_map = {}
    for i in range(len(nums)):
        print(nums[i])
        if target-nums[i] in hash_map:
            return[hash_map[target-nums[i]],i]
        hash_map[nums[i]]=i
    return []

nums = [3,2,4]
target = 6
print(twoSum(nums,target))
