class Solution(object):
    def maxCoins(self, nums):
        new_nums = [1]+[i for i in nums if i > 0]+[1]
        n = len(new_nums)
        dp = [[0]*n for _ in xrange(n)]
        for k in xrange(2,n):
            for l in xrange(0,n-k):
                r = l+k
                for m in xrange(l+1,r):
                    dp[l][r] = max(dp[l][r],new_nums[l]*new_nums[m]*new_nums[r]+dp[l][m]+dp[m][r])
        return dp[0][n-1]
