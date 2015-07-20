class Solution:    
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        def recur(temp, can, t):
            m = []
            for n in can:
                if n == can[0]:
                    m.append(n)
            if t > m[0]:
                for i in range(len(m)+1):
                    if t-m[0]*i == 0:
                        result.append(temp+[m[0]]*i)
                    else:
                        if len(can) > len(m):
                            recur(temp+[m[0]]*i, can[len(m):], t-m[0]*i)
            elif t == m[0]:
                result.append(temp+[m[0]])
        recur([], candidates, target)
        return result
                
a = Solution()
print a.combinationSum([1,1],2)

