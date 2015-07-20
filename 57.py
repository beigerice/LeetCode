class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
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
                
