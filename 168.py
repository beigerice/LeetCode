class Solution:
    def convertToTitle(self, num):
        temp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        s = 1
        t = 26
        while True:
            if num <= t:
                break
            s += 1
            t += 26**s            
        for i in xrange(s):
            idx = num//26**(s-i-1)
            if s-i > 1:
                if num%26**(s-i-1) == 0:
                    idx -= 1 
            result += temp[idx-1]
            num -= idx*26**(s-i-1)
        return result

a = Solution()
print a.convertToTitle(26*26+1)
