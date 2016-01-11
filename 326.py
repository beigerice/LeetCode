class Solution(object):
    def isPowerOfThree(self, n):
        return n>0 and abs(math.log(n, 3) - round(math.log(n, 3))) < 1e-10
