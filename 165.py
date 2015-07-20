class Solution:
    def compareVersion(self, version1, version2):
        v1 = map(int,version1.split('.'))
        v2 = map(int,version2.split('.'))
        while len(v1) > 0 and len(v2) > 0:
            if v1[0] > v2[0]:
                return 1
            elif v1[0] < v2[0]:
                return -1
            else:
                if len(v1) > 1 and len(v2) > 1:
                    v1 = v1[1:]
                    v2 = v2[1:]
                else:
                    if sum(v1) > sum(v2):
                        return 1
                    elif sum(v1) < sum(v2):
                        return -1
                    else:
                        return 0
                    

a = Solution()
print a.compareVersion('1.0.1.0','01.0.01.0')
