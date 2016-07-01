class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        if len(nums) == 1: return nums
        nums.sort()
        result = [[nums[0]]]
        toreturn = [nums[0]]
        for i in range(1,len(nums)):
            result.append([])
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    if len(result[j])+1 > len(result[i]):
                        result[i] = result[j]+[nums[i]]
                    if len(result[i]) > len(toreturn):
                        toreturn = result[i]
        return toreturn
