class Solution:
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        else:
            if s[0] == '0':
                return 0
            if len(s) == 1:
                return 1
            else:
                if s[1] == '0':
                    if s[0] == '1' or s[0] == '2': 
                        temp = [1,1]
                    else:
                        return 0
                else:
                    if int(s[:2]) <= 26:
                        temp = [1,2]
                    else:
                        temp = [1,1]
                for i in xrange(2,len(s)):
                    if s[i] == '0':
                        if s[i-1] == '1' or s[i-1] == '2':
                            temp[0],temp[1] = temp[1],temp[0]
                        else:
                            return 0
                    else:
                        if s[i-1] == '0' or int(s[i-1:i+1]) > 26:
                            temp[0],temp[1] = temp[1],temp[1]
                        else:
                            temp[0],temp[1] = temp[1],temp[0]+temp[1]
            return temp[-1]
                
a = Solution()
print a.numDecodings("227")
