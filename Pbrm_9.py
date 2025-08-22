#target of sums

def target_sum(nums,target):  
    hash_table={}

    for i in range(0,len(nums)):
        if target-nums[i] in hash_table:
            return [hash_table[target-nums[i]],i]
        hash_table[nums[i]]=i

nums = [3,2,4]
target = 6
print(target_sum(nums,target))
