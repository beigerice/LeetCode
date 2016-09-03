class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0)+1
        res = {}
        for i in t:
            res[i] = res.get(i,0)+1
        for k,v in res.iteritems():
            if k not in dic:
                return k
            if dic[k] < res[k]:
                return k
