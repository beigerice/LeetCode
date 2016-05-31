class Solution(object):
    def intersection(self, nums1, nums2):
        hashed_nums1 = set(nums1)
        res = set()
        for x in nums2: 
            if x in hashed_nums1: 
                res.add(x)
        return list(res)
