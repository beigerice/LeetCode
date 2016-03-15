class Solution(object):
    def increasingTriplet(self, nums):
        m0 = 2**32
        m1 = 2**32
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                m0 = min(m0,nums[i-1])
                if nums[i-1] > m0:
                    m1 = min(m1,nums[i-1])
                m1 = min(m1,nums[i])
            if nums[i] > m1:
                return True
        return False
