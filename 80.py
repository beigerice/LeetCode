class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        p = 1
        flag = 0
        for i in xrange(1,len(nums)):
            if nums[i] == nums[i-1]:
                if flag == 0:
                    nums[p] = nums[i]
                    p += 1
                    flag = 1
            else:                
                nums[p] = nums[i]
                p += 1
                flag = 0
        print nums
        return p

a = Solution()
print a.removeDuplicates([0,0,0,1,1,1,2,2,3,4,5,5,6,6,6,7,7,7,8])
