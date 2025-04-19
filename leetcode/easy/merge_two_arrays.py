'''
@author: Solrac
'''
def merger(nums1, m, nums2, n):
    p1 = m - n
    p2 = 0
    while p1 <= m-1 and p2 <= n-1:
        if nums1[p1] == 0:
            nums1[p1] = nums2[p2]
            p1 += 1
            p2 += 1
    return nums1
            
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [4, 5, 6]
print(merger(nums1, len(nums1), nums2, len(nums2)))