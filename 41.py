class Solution:
    def firstMissingPositive(self, A):
        i = 0
        j = len(A)-1
        while (i <= j):
            if i == A[i]-1:
                i += 1
            elif A[i] > j+1 or A[i] <= 0 or A[i] == A[A[i]-1]:
                A[i] = A[j]
                j -= 1 
            else:
                A[A[i]-1], A[i] = A[i], A[A[i]-1]
        return i+1    

a = Solution()
print a.firstMissingPositive([4,2,7,1,-2,3,0])
