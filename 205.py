class Solution:
    def isIsomorphic(self, s, t):
        dic = {}
        result = ''
        for i in xrange(len(s)):
            if dic.get(s[i]):
                if dic[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in dic.values():
                    dic[s[i]] = t[i]
                else:
                    return False
        return True

a = Solution()
print a.isIsomorphic('paper','title')
