'''
@author: Solrac
'''
def find_majority_num(nums):
    if nums != []:
        set1 = set(nums)
        list1 = list(set1)
        dict_ = dict()
        for num in list1:
            dict_[num] = nums.count(num)
            sortedList = list(sorted(dict_.items(), key=lambda x: x[1], reverse = True))
        return sortedList[0][0]

def find_majority_num_simple(nums):
    dictionary = {}
    for num in nums:
        dictionary[nums.count(num)] = num
    return dictionary[max(list(dictionary.keys()))]

nums = [2,2,1,1,1,2,2]
print(nums)
print(find_majority_num(nums))