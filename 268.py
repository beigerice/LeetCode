class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        s = len(nums)*(len(nums)+1)/2
        return s-sum(nums)
