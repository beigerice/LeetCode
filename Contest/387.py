class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        ref = set()
        cnt = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [i,cnt]
                cnt += 1
            else:
                ref.add(s[i])
        res = [-1,len(s)]
        for k,v in dic.iteritems():
            if v[1] < res[1] and k not in ref:
                res = v
        return res[0]

a = Solution()
print a.firstUniqChar("loveleetcode")
