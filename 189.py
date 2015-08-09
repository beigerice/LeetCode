class Solution:
    def rotate(self, nums, k):
        if k != 0 and len(nums) > 0:
            n = len(nums)
            if k >= n:
                k = k%n
            nums[:] = nums[-k:]+nums[:-k]
        print nums

a = Solution()
a.rotate([1,2],1)
