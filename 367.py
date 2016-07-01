class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 0
        high = num
        if num == 0: return False
        if num == 1: return True
        while low < high-1:
            mid = (low+high)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                high = mid
            else:
                low = mid
        return False        
