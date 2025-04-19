'''
@author: Solrac
'''
def find4sum(nums, x):
    nums.sort()
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            s = j + 1
            e = len(nums) - 1
            while s < e:
                if nums[s] + nums[e] + nums[i] + nums[j] == x:
                    print(nums[s], nums[e], nums[i], nums[j])
                    s += 1
                    e -= 1
                elif nums[s] + nums[e] + nums[i] + nums[j] < x:
                    s += 1
                else:
                    e -= 1
                    
nums = [1, 4, 45, 6, 10, 12]
x = 21
print(nums)
print(find4sum(nums, x))