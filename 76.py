class Solution:
    def minWindow(self, s, t):
        dic = {}
        for letter in t:
            if letter in dic:
                dic[letter][0] += 1
            else:
                dic[letter] = [1,0]
        cnt = 0
        temp = []
        result = [0,len(s)]
        for i in xrange(len(s)):
            if s[i] in dic:
                if dic[s[i]][1] < dic[s[i]][0]:
                    cnt += 1
                dic[s[i]][1] += 1
                temp.append(i)
            if cnt == len(t):                
                j = 0
                while dic[s[temp[j]]][1] > dic[s[temp[j]]][0]:
                    dic[s[temp[j]]][1] -= 1
                    j += 1
                temp = temp[j:]
                if temp[-1]-temp[0] <= result[-1]-result[0]:
                    result[0],result[-1] = temp[0],temp[-1]                     
                dic[s[temp[0]]][1] -= 1
                temp = temp[1:]
                cnt -= 1
        if result[1] < len(s):
            return s[result[0]:result[-1]+1]
        else:
            return ''

a = Solution()
print a.minWindow("aa","aa")
                            
                            
