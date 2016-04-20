class Solution(object):
    def minCut(self, s):
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1        
        refer = [0]
        for i in range(1,len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                refer.append(0)
            else:
                refer.append(refer[i-1]+1)
                for j in range(1,i):
                    if s[j:i+1] == s[j:i+1][::-1]:
                        refer[i] = min(refer[i],refer[j-1]+1)
        return refer[-1]
