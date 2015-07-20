from math import log

class Solution:
    def trailingZeroes(self, n):
        if n < 5:
            return 0
        else:
            result = n//5
            s = int(log(n,5))
            for i in xrange(2,s+1):
                result += n//(5**i)
            return result

a = Solution()
print a.trailingZeroes(200)

