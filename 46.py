class Solution:
    def permute(self, nums):
        def factorial(x):
            y = 1
            for i in xrange(1,x+1):
                y *= i
            return y
        result = []
        n = len(nums)
        for i in xrange(factorial(n)):
            result.append([])
        for i in xrange(n):
            idx = i
            for j in xrange(factorial(n)):
                if idx >= n:
                    idx = i+
                result[i][idx+j] = nums[i]
                idx += 1
        return result
            
a = Solution()
print a.permute([1,2,3])
        
        
