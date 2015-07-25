class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        if s == '':
            return True
        i = 0
        j = len(s)-1
        while True:
            if i >= j:
                return True
            while s[i].isalnum() == False:
                if i == j:
                    return True
                i += 1
            while s[j].isalnum() == False:
                j -= 1
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1

a = Solution()
print a.isPalindrome(".,")
