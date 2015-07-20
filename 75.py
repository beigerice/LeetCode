class Solution:
    def sortColors(self, A):
        if len(A) > 0:
            i = 0
            j = len(A)-1
            while i < j:
                if A[i] == 0:
                    i += 1
                else:
                    if A[j] == 0:
                        A[i],A[j] = A[j],A[i]
                    j -= 1
            j = len(A)-1
            while i < j:
                if A[j] == 2:
                    j -= 1
                else:
                    if A[i] == 2:
                        A[i],A[j] = A[j],A[i]
                    i += 1
        print A
        

a = Solution()
a.sortColors([0])
