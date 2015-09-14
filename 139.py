class Solution(object):
    def wordBreak(self, s, wordDict):
        result = [0]*len(s)
        for i in xrange(len(s)):
            for word in wordDict:
                if i+1 > len(word):
                    if s[i+1-len(word):i+1] == word:
                        if result[i-len(word)] == 1:
                            result[i] = 1
                            break
                elif i+1 == len(word):
                    if s[i+1-len(word):i+1] == word:
                        result[i] = 1
                        break
        if result[-1]:
            return True
        else:
            return False
        
a = Solution()
print a.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
        
