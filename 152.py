class Solution:
    def maxProduct(self, A):
        f = [A[0]]
        g = [A[0]]
        for i in xrange(1,len(A)):
            f.append(max(f[i-1]*A[i],A[i],g[i-1]*A[i]))
            g.append(min(g[i-1]*A[i],A[i],f[i-1]*A[i]))
        return max(f)

a = Solution()
print a.maxProduct([-4,-3,-2])
