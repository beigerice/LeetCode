class Solution:
    def longestConsecutive(self, num):
        dic = {}
        duplicate = {}
        for i in num:
            if i not in duplicate:
                duplicate[i] = 0
                if i-1 in dic and i+1 in dic:
                    dic[dic[i-1]],dic[dic[i+1]] = dic[i+1],dic[i-1]
                elif i-1 in dic:
                    dic[dic[i-1]],dic[i] = i,dic[i-1]
                elif i+1 in dic:
                    dic[dic[i+1]],dic[i] = i,dic[i+1]
                else:
                    dic[i] = i
        result = 0
        for k,v in dic.iteritems():
            result = max(result,abs(k-v)+1)
        return result

a = Solution()
print a.longestConsecutive([-2,-1,0,1,2,3,4,5,6])
            
