class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        elif len(prices) == 2:
            if prices[1] > prices[0]:
                return prices[1]-prices[0]
            else:
                return 0
        else:
            result = 0
            if prices[0] <= prices[1]:
                valley = prices[0]
            for i in xrange(1,len(prices)-1):
                if prices[i] > prices[i-1] and prices[i] >= prices[i+1]:
                    peak = prices[i]
                    result += peak-valley
                if prices[i] <= min(prices[i-1],prices[i+1]):
                    valley = prices[i]
            if prices[-1] > prices[-2]:
                result += prices[-1]-valley
            return result

a = Solution()
print a.maxProfit([5,2,3,2,6,6,2,9,1,0,7,4,5,0])
