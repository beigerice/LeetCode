from math import sqrt
class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        else:
            temp = [1]*n
            for i in xrange(2,int(sqrt(n))+1):
                if temp[i] == 1:
                    for j in xrange(i*i,n,i):
                        temp[j] = 0
            return sum(temp)-2            

a = Solution()
print a.countPrimes(5)
