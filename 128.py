class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num.sort()
        result = 0
        temp = [num[0]]
        for i in range(1,len(num)):
            if num[i] - num[i-1] > 1:
                if len(temp) > result:
                    result = len(temp)
                temp = [num[i]]
            elif num[i] == num[i-1]:
                continue
            else:
                temp.append(num[i])
        if len(temp) >  result:
            result = len(temp)
        return result

a = Solution()
print a.longestConsecutive([1,2,0,1])
