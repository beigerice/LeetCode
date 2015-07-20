class Solution:
    def isValid(self, s):
        dic = {'(':')','{':'}','[':']'}
        temp = []
        for i in s:
            if i in dic:
                temp.append(dic[i])
            else:
                if not temp or temp.pop() != i:
                    return False
        return not temp

a = Solution()
print a.isValid('[')
