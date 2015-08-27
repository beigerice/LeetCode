class Solution:
    def permute(self, nums):
        def f(x):
            return x * f(x-1) if x >1 else 1
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [nums,[nums[1],nums[0]]]
        else:

a = Solution()
print a.permute([1,2,3])
        
        
