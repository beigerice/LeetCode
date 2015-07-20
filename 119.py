import operator
class Solution:
    def getRow(self, rowIndex):
        def c(n,k):
            return  reduce(operator.mul,range(n-k+1,n+1))/reduce(operator.mul,range(1,k+1))
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            result = [0]*(rowIndex+1)
            result[0] = 1
            result[-1] = 1            
            for i in xrange(rowIndex-1):
                result[i+1] = c(rowIndex,i+1)
            return result

a = Solution()
print a.getRow(4)
