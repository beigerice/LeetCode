class Solution:
    def numDistinct(self, s, t):
        if len(s) == 0:
            return 0
        temp1 = [0]*len(s)
        for x in xrange(len(s)):
            if s[x] == t[0]:
                temp1[x] = temp1[x-1]+1
            else:
                temp1[x] = temp1[x-1]
        for i in xrange(1,len(t)):
            temp2 = [0]*len(s)
            for j in xrange(i,len(s)):
                if s[j] == t[i]:
                    temp2[j] = temp1[j-1]+temp2[j-1]
                else:
                    temp2[j] = temp2[j-1]
            temp1 = temp2
            print temp1
        return temp1[-1]
a = Solution()
print a.numDistinct('ccc','c')
