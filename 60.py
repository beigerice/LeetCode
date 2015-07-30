class Solution:
    def getPermutation(self, n, k):
        def factorial(x):
            y = 1
            for i in xrange(1,x+1):
                y *= i
            return y
        result = ''
        nlist = []
        for i in xrange(n):
            nlist.append(i+1)
        k -= 1
        for i in xrange(n-1,-1,-1):
            temp = k//factorial(i)
            result += str(nlist[temp])
            del nlist[temp]
            k -= temp*factorial(i)
        return result

a = Solution()
print a.getPermutation(1,1)
