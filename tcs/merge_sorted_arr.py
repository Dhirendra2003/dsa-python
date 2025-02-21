class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1 = nums1[0:m] + nums2
        nums1.sort()
        print(nums1)
        nums1.clear()


s=Solution()
s.merge([1,2,3,0,0,0],3,[2,5,6],3)
)