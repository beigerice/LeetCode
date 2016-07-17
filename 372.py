class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        apower = a
        for digit in reversed(b):
            res = res * pow(apower,digit,1337)%1337
            apower = pow(apower,10,1337)
        return res
