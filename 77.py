class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        for i in xrange(1,n+1):
            result.append([i])
        for cnt in xrange(2,k+1):
            temp = []
            for i in xrange(len(result)):
                for j in xrange(result[i][-1]+1,n+1):
                    temp.append(result[i]+[j])
            result = temp
        return result

a = Solution()
print a.combine(5,3)
        
