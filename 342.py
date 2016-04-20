class Solution(object):
    def isPowerOfFour(self, num):
        return num > 0 and abs(math.log(num, 4) - round(math.log(num, 4))) < 1e-10
