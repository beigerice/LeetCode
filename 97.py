class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s3) >= 1 and len(s1) >= 1 and len(s2) >= 1:
            temp = []
            if s1[0] == s3[0]:
                temp.append([1,0])
            if s2[0] == s3[0]:
                temp.append([0,1])
            for i in xrange(1,len(s3)):
                mv = []
                for j in xrange(len(temp)):
                    if temp[j][0] < len(s1):
                        if s1[temp[j][0]] == s3[i]:
                            if [temp[j][0]+1,temp[j][1]] not in mv:
                                mv.append([temp[j][0]+1,temp[j][1]])
                    if temp[j][1] < len(s2):
                        if s2[temp[j][1]] == s3[i]:
                            if [temp[j][0],temp[j][1]+1] not in mv:
                                mv.append([temp[j][0],temp[j][1]+1])
                temp = mv
                if temp == []:
                    return False
            return True
        else:
            if s1 == s3:
                return True
            if s2 == s3:
                return True
            return False

a = Solution()
print a.isInterleave("", "", "")
