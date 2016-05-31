class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def bs(n):
            low = 0
            high = k-1
            while low <= high:
                mid = (low+high)//2
                if temp[mid] > n:
                    low = mid+1
                elif temp[mid] < n:
                    high = mid-1
                else:
                    return mid
            return low        
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0)+1
        temp = [0]*k
        result = [-1]*k
        for key,value in dic.iteritems():
            if value > temp[-1]:
                idx = bs(value)
                temp.insert(idx,value)
                temp.pop()
                result.insert(idx,key)
                result.pop()
        return result
