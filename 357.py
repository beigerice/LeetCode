class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        result = 10
        while n > 1:
            end = 9-n+2
            temp = 9
            m = 9
            while m >= end:
                temp *= m
                m -= 1
            result += temp
            n -= 1
        return result
