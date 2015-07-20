def findMedianSortedArrays(A, B):
    def findkth(a,b,k):
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

    if (len(A)+len(B))%2 == 0:
        return (findkth(A,B,(len(A)+len(B))//2)+findkth(A,B,(len(A)+len(B))//2+1))*0.5
    else:
        return findkth(A,B,(len(A)+len(B))//2+1)

print findMedianSortedArrays([1,2,3,4,6],[2,3])
