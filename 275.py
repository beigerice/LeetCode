class Solution(object):
    def hIndex(self, citations):
        if len(citations) == 0:
            return 0
        low = 0
        high = len(citations)-1
        while low <= high:
            mid = (low+high)//2
            if citations[mid] < len(citations)-mid:
                low = mid+1
            elif citations[mid] > len(citations)-mid:
                high = mid-1
            else:
                return len(citations)-mid
        if citations[mid] < len(citations)-mid:
            return len(citations)-mid-1
        else:
            return len(citations)-mid

a = Solution()
print a.hIndex([0])
