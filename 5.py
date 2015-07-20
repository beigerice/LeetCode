def isPalindrome(s):
    while len(s) >= 2:
        if s[0] != s[-1]:
            return False
        else:
            s = s[1:len(s)-1]
    return True
class Solution:
    def longestPalindrome(self, s):
        for i in xrange(len(s),0,-1):
            for j in xrange(0,len(s)-i+1):
                if isPalindrome(s[j:j+i]):
                    return s[j:j+i] 
                
a = Solution()
