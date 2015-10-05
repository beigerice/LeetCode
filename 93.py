class Solution(object):
    def restoreIpAddresses(self, s):
        def dfs(d,n):
            if n == 1:
                if len(d) == 0:
                    return []
                if int(d) > 255:
                    return []
                if d[0] == '0' and len(d) > 1:
                    return []
                return [d]
            else:
                result = []
                if len(d) == 0:
                    return result                
                if d[0] == '0':
                    for i in dfs(d[1:],n-1):
                        result.append('0.'+i)
                else:
                    for i in dfs(d[1:],n-1):
                        result.append(d[:1]+'.'+i)
                    for i in dfs(d[2:],n-1):
                        result.append(d[:2]+'.'+i)
                    for i in dfs(d[3:],n-1):
                        if int(d[:3]) <= 255:
                            result.append(d[:3]+'.'+i)
                return result
        return dfs(s,4)

a = Solution()
print a.restoreIpAddresses('10000')
