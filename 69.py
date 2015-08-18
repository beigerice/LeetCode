class Solution:
    def mySqrt(self, x):
        low = 0
        high = x
        if x < 2:
            return x
        while low < high-1:
            mid = (low+high)//2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                high = mid
            else:
                low = mid
        return low

a = Solution()
print a.mySqrt(1)
