class Solution:
    def summaryRanges(self, nums):
        result = []
        if len(nums) == 0:
            return result        
        temp = str(nums[0])
        for i in xrange(1,len(nums)):
            if nums[i] != nums[i-1]+1:
                if temp == str(nums[i-1]):
                    result.append(temp)
                else:
                    result.append(temp+'->'+str(nums[i-1]))
                temp = str(nums[i])
        if temp != str(nums[-1]):
            result.append(temp+'->'+str(nums[-1]))
        else:
            result.append(temp)
        return result

a = Solution()
print a.summaryRanges([0])
