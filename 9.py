class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        flag = 1
        while x/flag >= 10:
            flag *= 10
        if flag == 1:
            return True
        else:
            while flag >= 1:
                x = int((x-x%10*flag)/10)
                flag /= 100
            if x == 0:
                return True
            else:
                return False

a = Solution()
print a.isPalindrome(1221)
