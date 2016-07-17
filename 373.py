class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        heap = []
        for i in nums1:
            heap.append([i+nums2[0],i,0])
        res = []
        while len(res) < k and heap:
            total,n,idx = heap[0]
            res.append([n,total-n])
            if idx == len(nums2)-1:
                heapq.heappop(heap)
            else:
                heapq.heapreplace(heap,[n+nums2[idx+1],n,idx+1])
        return res
