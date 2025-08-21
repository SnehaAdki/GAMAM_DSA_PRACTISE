#total Container 

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
