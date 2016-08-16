class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        new = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                new.append(nums[i])
        res = 2
        for i in range(1,len(new)-1):
            if new[i] > new[i-1] and new[i] > new[i+1]:
                res += 1
            elif new[i] < new[i-1] and new[i] < new[i+1]:
                res += 1
        return res
