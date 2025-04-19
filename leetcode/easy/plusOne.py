'''
@author: Solrac
'''
def adding_plusone_to_listToDigit(nums):
    num = [1,2,3]
    numstr = str(num).strip('[')
    numstr = numstr.strip(']')
    numstr = numstr.replace(', ', '')
    numint = int(numstr) 
    numint += 1
    num = [int(element) for element in str(numint)]
    return num

nums = [1, 2, 3]
print(nums)
print(adding_plusone_to_listToDigit(nums))

