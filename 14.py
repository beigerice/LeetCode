class Solution:
    def longestCommonPrefix(self, strs):
        result = ''
        if len(strs) == 0:
            return result
        for i in xrange(len(strs[0])):
            for j in xrange(1,len(strs)):
                if i > len(strs[j])-1:
                    return result
                else:
                    if strs[0][i] != strs[j][i]:
                        return result
            result += strs[0][i]
        return result

a = Solution()
print a.longestCommonPrefix(['','aac','aad'])

