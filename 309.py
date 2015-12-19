class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        buy,sell,pre_buy,pre_sell = -prices[0],0,0,0
        for price in prices:
            pre_buy = buy
            buy = max(pre_sell-price,pre_buy)
            pre_sell = sell
            sell = max(pre_buy+price,pre_sell)
        return sell
