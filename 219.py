class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) <= k:
            return len(set(nums)) < len(nums)
        dic = {}
        for i in xrange(k+1):
            if nums[i] in dic:
                return True
            else:
                dic[nums[i]] = 0
        for i in xrange(k+1,len(nums)):
            del dic[nums[i-k-1]]
            if nums[i] in dic:
                return True
            else:
                dic[nums[i]] = 0
        return False

a = Solution()
print a.containsNearbyDuplicate([1,2,1],0)
