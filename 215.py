class Solution:
    def findKthLargest(self, nums, k):
        if len(a) > len(b):
            return findkth(b,a,k)
        if len(a) == 0:
            return b[k-1]
        if k == 1:
            return min(a[0],b[0])
        parta = min(k//2,len(a))
        partb = k-parta
        if a[parta-1] < b[partb-1]:
            return findkth(a[parta:],b,k-parta)
        else:
            return findkth(a,b[partb:],k-partb)        
