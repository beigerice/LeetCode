class Solution(object):
    def firstBadVersion(self, n):
        low = 1
        high = n
        while low < high-1:
            mid = (low+high)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid
        if isBadVersion(low):
            return low
        elif isBadVersion((low+high)//2):
            return mid
        else:
            return high

a = Solution()
def isBadVersion(n):
    if n >= 2:
        return True
    else:
        return False
print a.firstBadVersion(2)

