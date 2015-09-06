class Solution(object):
    def longestValidParentheses(self, s):
        pos = 0
        neg = 0
        result = 0
        for i in xrange(len(s)):
            if s[i] == '(':
                pos += 1
            else:
                neg += 1
            if pos == neg:
                result = max(result,pos+neg)
            elif pos < neg:
                pos = 0
                neg = 0
        pos = 0
        neg = 0
        for i in xrange(len(s)-1,-1,-1):
            if s[i] == ')':
                pos += 1
            else:
                neg += 1
            if pos == neg:
                result = max(result,pos+neg)                
            elif pos < neg:
                pos = 0
                neg = 0
        return result

a = Solution()
print a.longestValidParentheses("()(()")
