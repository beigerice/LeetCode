class Solution:
    def isHappy(self, n):
        temp = {}
        temp[n] = 0
        while True:
            m = 0
            for i in str(n):
                m += int(i)**2
            n = m
            if n == 1:
                return True
            else:
                if n not in temp:
                    temp[n] = 0
                else:
                    return False

a = Solution()
print a. isHappy(0)
