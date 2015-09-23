class Solution(object):
    def moveZeroes(self, nums):
        cnt = -1
        for i in xrange(len(nums)):
            if nums[i] != 0:
                cnt += 1
                if i != cnt:
                    nums[i],nums[cnt] = nums[cnt],nums[i]
