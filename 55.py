class Solution:
    def canJump(self, A):
        if len(A) == 1:
            return 0
        else:
            if A[0] >= len(A)-1:
                return 1
            else:
                result = 1
                idx1 = 1
                idx2 = A[0]            
                while True:
                    m = 0
                    result += 1
                    for i in xrange(idx1,idx2+1):
                        m = max(m,A[i]+i)
                        if m >= len(A)-1:
                            return result
                    idx1,idx2 = idx2,m
                
           
        
a = Solution()
test = []
for i in xrange(1000000):
    test.append(1)
print a.canJump([1,2])
