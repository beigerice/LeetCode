class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x == z or y == z:
            return True
        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b != 0:
                temp = a % b
                a = b
                b = temp
            return a
        temp = gcd(x,y)
        if temp == 1:
            return z < max(x,y)
        else:
            return z < max(x,y) and z%temp == 0
