class Solution:
    def findSubstring(self, s, words):
        result = []
        l = len(words[0])
        m = len(words)
        dic = {}
        for word in words:
            dic[word] = dic.get(word,0)+1
        for i in xrange(l):
            while i <= len(s)-l*m:
                if i < l:
                    temp = {}
                    for j in xrange(i,i+l*m,l):
                        temp[s[j:j+l]] = temp.get(s[j:j+l],0)+1
                else:
                    temp[s[i+l*(m-1):i+l*m]] = temp.get(s[i+l*(m-1):i+l*m],0)+1
                if temp == dic:
                    result.append(i)
                if temp[s[i:i+l]] == 1:
                    del temp[s[i:i+l]]
                else:
                    temp[s[i:i+l]] -= 1                    
                i += l
        return result

a = Solution()
