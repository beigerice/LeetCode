class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) <= 3:
            return max(nums)
        else:
            r0 = nums[0]
            r1 = nums[1]
            r2 = max(nums[0],nums[1])
            r3 = max(nums[1],nums[2])
            r4 = max(nums[0]+nums[2],nums[1])
            r5 = max(nums[0],nums[1],nums[2])
            for i in xrange(3,len(nums)):
                r0,r1,r2,r3,r4,r5 = r2,r3,max(r0+nums[i-1],r2),max(r1+nums[i],r3),max(r2+nums[i],r4),max(r1+nums[i],r4)
            return r5

a = Solution()
print a.rob([2,1,1,1])
            
