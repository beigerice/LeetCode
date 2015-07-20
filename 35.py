class Solution:
    def searchInsert(self, A, target):
        top,bottom = 0,len(A)-1
        idx = (bottom+top)//2
        while True:
            if A[idx] == target:
                return idx
            elif A[idx] > target:
                if bottom == idx:
                    if A[top] >= target: return top
                    else: return top+1
                else:
                    bottom = idx
                    idx = (bottom+top)//2
            else:
                if top == idx:
                    if A[bottom] == target: return bottom
                    elif A[bottom] < target: return bottom+1
                    else: return top+1
                else:
                    top = idx
                    idx = (bottom+top)//2
a = Solution()
print a.searchInsert([1,3,5,6],0)
