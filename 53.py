class Solution:
    def maxSubArray(self, A):
        result = 0
        temp = 0
        for i in xrange(len(A)):
            if A[i]+temp > 0:
                temp += A[i]
                result = max(result,temp)
            else:
                temp = 0
        if result == 0:
            return max(A)
        return result

a = Solution()
print a.maxSubArray([1,2,3,4,5])
