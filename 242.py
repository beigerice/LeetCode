class Solution:
    def isAnagram(self, s, t):
        temp = {}
        for i in s:
            temp[i] = temp.get(i,0)+1
        for j in t:
            if j in temp:
                if temp[j] > 0:
                    temp[j] -= 1
                else:
                    return False
            else:
                return False
        for k,v in temp.iteritems():
            if v > 0:
                return False
        return True

a = Solution()
print a.isAnagram('ab','a')
