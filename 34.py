class Solution:
    def searchRange(self, A, target):
        top,bottom = 0,len(A)-1
        idx = (bottom+top)//2
        while True:
            if A[idx] == target:
                index1,index2 = idx,idx
                while index1 >= 0:
                    if A[index1] != target:
                        index1 += 1
                        break               
                    index1 -= 1
                while index2 <= len(A)-1:
                    if A[index2] != target:
                        index2 -= 1
                        break               
                    index2 += 1
                return [index1,index2]
            elif A[idx] > target:
                if bottom == idx:
                    if A[top] == target: return [top,top]
                    else: return [-1,-1]
                else:
                    bottom = idx
                    idx = (bottom+top)//2
            else:
                if top == idx:
                    if A[bottom] == target: return [bottom,bottom]
                    else: return [-1,-1]
                else:
                    top = idx
                    idx = (bottom+top)//2
            
a = Solution()
print a.searchRange([3,3,4,5,6,7,8],2)
