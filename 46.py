class Solution:   
    def permute(self, nums):        
        result = [[nums[0]]]
        for i in xrange(1,len(nums)):
            temp = []
            for way in result:
                for j in xrange(len(way)):
                    temp.append(way[:j]+[nums[i]]+way[j:])
                temp.append(way+[nums[i]])
            result = temp
        return result
    
a = Solution()
print a.permute([1,2,3,4,5,6])
        
        
