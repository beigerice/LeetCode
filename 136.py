class Solution:
    def singleNumber(self, A):
        temp = A[0]
        for i in xrange(1,len(A)):
            temp ^= A[i]
        return temp

a = Solution()
print a.singleNumber([1,2,2])
