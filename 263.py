class Solution:
    def isUgly(self, num):
        if num == 0:
            return False
        while num%2 == 0:
            num /= 2
        while num%3 == 0:
            num /= 3
        while num%5 == 0:
            num /= 5
        if num == 1:
            return True
        else:
            return False

a = Solution()
print a.isUgly(14)
