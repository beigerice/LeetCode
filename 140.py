class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        dp = []
        for i in xrange(len(s)+1):
            dp.append([])
        for i in xrange(1,len(s)+1):
            if s[:i] in wordDict:
                dp[i].append(0)
            for j in xrange(i):
                if len(dp[j]) > 0 and s[j:i] in wordDict:
                    dp[i].append(j)
        result = []
        def dfs(temp,i):
            if i == 0:
                result.append(temp)
            if len(dp[i]) > 0:
                for j in dp[i]:
                    dfs(temp+[i],j)
        dfs([],len(dp)-1)
        toreturn = []
        for i in result:
            for j in xrange(len(i)-1,-1,-1):
                if j == len(i)-1:
                    temp = s[:i[j]]
                else:
                    temp += ' '+s[i[j+1]:i[j]]
            toreturn.append(temp)
        return toreturn
