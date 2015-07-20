class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x:(x.start,-x.end))
        result = [intervals[0]]      
        for i in xrange(1,len(intervals)):
            if intervals[i].start != intervals[i-1].start:
                if intervals[i].start <= result[-1].end:
                    if intervals[i].end > result[-1].end:
                        result[-1].end = intervals[i].end
                else:
                    result.append(intervals[i])
        return result
            
a = Solution()
a.merge([Interval(2,6),Interval(1,3),Interval(1,2),Interval(8,10),Interval(15,18)])
