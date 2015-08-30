class Solution(object):
    def permuteUnique(self, nums):
        dic = {}
        dic[repr(nums)] = 1
        result = [nums]
        for i in xrange(len(nums)-2,-1,-1):
            for k in xrange(len(result)):
                for j in xrange(i+1,len(nums)):
                    temp = result[k][:]
                    if temp[i] != temp[j]:
                        temp[i],temp[j] = temp[j],temp[i]
                        if repr(temp) not in dic:
                            result.append(temp)
                            dic[repr(temp)] = 1
        return len(result)
    
a = Solution()
print a.permuteUnique([3,3,0,0,2,3,2])
