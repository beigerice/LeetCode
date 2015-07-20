class Solution: 
    def maxProfit(self, k, prices):
        if len(prices) <= 1:
            return 0
        else:
            if k == 0:
                return 0
            else:
                valley = []
                peak = []
                if prices[0] < prices[1]:
                    valley.append(prices[0])            
                for i in xrange(1,len(prices)-1):
                    if prices[i] < prices[i+1] and prices[i] <= prices[i-1]:               
                        valley.append(prices[i])
                    if prices[i] > prices[i-1] and prices[i] >= prices[i+1]:
                        peak.append(prices[i])
                if prices[-1] > prices[-2]:
                    peak.append(prices[-1])
                while len(peak) > k:
                    mv = peak[0]-valley[0]
                    idx1 = 0
                    idx2 = 0
                    for i in xrange(len(peak)):
                        if peak[i]-valley[i] < mv:
                            mv = peak[i]-valley[i]
                            idx1 = i
                            idx2 = i
                        if i != len(peak)-1:
                            if peak[i]-valley[i+1] < mv:
                                mv = peak[i]-valley[i+1]
                                idx1 = i+1
                                idx2 = i
                    del valley[idx1],peak[idx2]
            return sum(peak)-sum(valley)

a = Solution()
print a.maxProfit(2,[4,3])
