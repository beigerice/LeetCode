class Solution:
    def findSubstring(self, s, words):
        result = []
        l = len(words[0])
        m = len(words)
        dic = {}
        for word in words:
            dic[word] = dic.get(word,0)+1
        for i in xrange(len(s)-l*m+1):
            temp = {}
            for j in xrange(i,i+l*m,l):
                if s[j:j+l] in dic:
                    temp[s[j:j+l]] = temp.get(s[j:j+l],0)+1
            if temp == dic:
                result.append(i)
        return result

a = Solution()
print a.findSubstring("barfoothefoobarman",["foo","bar"])
        
            
