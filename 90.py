class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        dic = {}
        result = []
        for i in xrange(len(nums)):
            result.append([i])
        toreturn = result
        for cnt in xrange(2,len(nums)):
            temp = []
            for i in xrange(len(result)):
                for j in xrange(result[i][-1]+1,len(nums)):
                    temp.append(result[i]+[j])
            result = temp
            toreturn += result
        result = []
        for i in xrange(len(toreturn)):
            for j in xrange(len(toreturn[i])):
                toreturn[i][j] = nums[toreturn[i][j]]
            if repr(toreturn[i]) not in dic:
                result.append(toreturn[i])
                dic[repr(toreturn[i])] = 1
        result.append([])
        if len(nums) > 1:
            result.append(nums)
        return result

a = Solution()
print a.subsetsWithDup([1,1,2,2])
