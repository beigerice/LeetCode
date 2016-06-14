# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dic = {}
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val not in self.dic:
            self.dic[val] = 1
            low = 0
            high = len(self.arr)
            while low < high:
                mid = (low+high)//2
                if self.arr[mid] < val:
                    low = mid+1
                else:
                    high = mid
            self.arr.insert(low,val)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        result = [[self.arr[0],self.arr[0]]]
        for i in range(1,len(self.arr)):
            if self.arr[i] != self.arr[i-1]+1:
                result.append([self.arr[i],self.arr[i]])
            else:
                result[-1][1] = self.arr[i]
                
        return result
