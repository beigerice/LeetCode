class Solution:
    def singleNumber(self, A):
        a = 0
        b = 0
        for i in xrange(len(A)):
            b ^= a&A[i]
            a ^= A[i]
            c = ~(a&b)
            a &= c
            b &= c
        return a

a = Solution()
print a.singleNumber([1,2,2,2,3,3,3])

