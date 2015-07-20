class Solution:
    def lengthOfLastWord(self, s):
        try:
            s.split()[-1]
            return len(s.split()[-1])
        except Exception, e:
            return 0

a = Solution()
print a.lengthOfLastWord('   ')
