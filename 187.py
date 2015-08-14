class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        result = []
        temp = s[:10]
        dic = {}
        dic[temp] = 1
        for i in xrange(10,len(s)):
            temp = temp[1:]+s[i]
            dic[temp] = dic.get(temp,0)+1
        for k,v in dic.iteritems():
            if v > 1:
                result.append(k)
        return result

a = Solution()
print a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
