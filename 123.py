class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        else:
            n = prices[0]
            ke = 0        
            temp = [0]*len(prices) 
            for i in xrange(len(prices)):
                n = min(n,prices[i])
                ke = max(ke,prices[i]-n)
                temp[i] = ke
            m = 0
            la = 0
            temp_reverse = [0]*len(prices)
            for i in xrange(len(prices)-1,-1,-1):
                m = max(m,prices[i])
                la = max(la,m-prices[i])
                temp_reverse[i] = la
            result = 0
            for i in xrange(len(prices)-1):
                result = max(result,temp[i]+temp_reverse[i+1])
            result = max(result,temp[-1])
            return result

a = Solution()
print a.maxProfit([1,2,3,6,1,6])
