# max of container trapped

def container(nums):
    max_area = 0
    curr_area = 0
    left = 0
    right = len(nums)-1

    while left < right:
        curr_area = min(nums[left],nums[right])* (right-left)
        if nums[left]<nums[right]:
            left+=1
        else:
            right-=1
        max_area = max(curr_area,max_area)
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(container(height))
