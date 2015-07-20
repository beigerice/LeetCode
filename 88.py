class Solution:
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        while n > 0:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
        print nums1

a = Solution()
a.merge([0,1,3,4,0,0,0,0],4,[1,2,4,7],4)
