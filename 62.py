class Solution:
    def uniquePaths(self, m, n):
        def factorial(x):
            result = 1
            for i in xrange(1,x+1):
                result *= i
            return result
        return factorial(m+n-2)/factorial(m-1)/factorial(n-1)

a = Solution()
print a.uniquePaths(1,2)
        
