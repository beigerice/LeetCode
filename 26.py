class Solution:
    def removeDuplicates(self, A):
        if not A:
            return 0
        p = 1
        for i in range(1,len(A)):
            if A[i] != A[i-1]:
                A[p] = A[i]
                p += 1
        return p

a = Solution()
print a.removeDuplicates([1,2,3,3])
