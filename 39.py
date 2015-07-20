class Solution:    
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        def recur(temp, can, t):
            m = can[0]
            if t > m:
                for i in range(t//m+1):
                    if t-m*i == 0:
                        result.append(temp+[m]*i)
                    else:
                        if len(can) > 1:
                            recur(temp+[m]*i, can[1:], t-m*i)
            elif t == m:
                result.append(temp+[m])
        recur([], candidates, target)
        return result
                
a = Solution()
print a.combinationSum([1],2)

