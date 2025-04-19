'''
@author: Solrac
'''
def rotate_right(nums, k):
    for i in range(k):
        addnum = nums[len(nums)-1]
        nums.reverse()
        nums.append(addnum)
        nums.reverse()
        nums.pop()
    return nums

k = 3
nums = [1,2,3,4,5,6,7]
print(nums)
print(rotate_right(nums, k))