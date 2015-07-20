class Solution:
    def reverseWords(self, s):
        s.strip('')
        temp = s.split()
        result = ''
        if len(temp) > 0:            
            for i in xrange(len(temp)-1,0,-1):
                result += temp[i]+' '
            result += temp[0]
        return result

a = Solution()
print a.reverseWords('a b')
