class Solution:
    def maxProfit(self, prices):
        m = 0
        result = 0
        for i in xrange(len(prices)-1,-1,-1):
            m = max(m,prices[i])
            result = max(result,m-prices[i])
        return result

a = Solution()
print a.maxProfit([1,3,4,2,5])
