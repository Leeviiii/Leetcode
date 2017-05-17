# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "start is %d,end is %d" % (self.start,self.end)

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        if newInterval == None:
            return intervals
        l = 0
        r = len(intervals) - 1
        while l <= r:
            if l == r:
                if intervals[l].start < newInterval.start:
                    intervals.insert(l+1,newInterval)
                else:
                    intervals.insert(l,newInterval)
                break
            if l + 1 == r:
                if intervals[l].start > newInterval.start:
                    intervals.insert(l,newInterval) 
                elif intervals[r].start < newInterval.start:
                    intervals.insert(r+1,newInterval)
                else:
                    intervals.insert(r,newInterval)
                break
            m = (l+r)/2
            if intervals[m].start <= newInterval.start:
                if intervals[m+1].start >= newInterval.start:
                    intervals.insert(m+1,newInterval)  
                    break
                l = m
            else:
                if intervals[m-1].start <= newInterval.start:
                    intervals.insert(m,newInterval) 
                    break
                r = m
        for i in intervals:
            print i
        ret = []
        for i in range(1,len(intervals)):
            if intervals[i].start > intervals[i-1].end:
                ret.append(intervals[i-1])
            else:
                intervals[i].start = intervals[i-1].start
                intervals[i].end = max(intervals[i].end,intervals[i-1].end)
        ret.append(intervals[len(intervals)-1])
        return ret


if __name__ == "__main__": 
    s = Solution()
    s1 = Interval(0,3)
    s2 = Interval(5,8)
    s3 = Interval(9,11)
    s4 = Interval(8,10)
    s5 = Interval(12,16)
    s6 = Interval(1,1)
    s7 = Interval(3,5)
    s8 = Interval(2,2)
    new = Interval(9,18)
    inputs = [s1,s2,s3,s4,s5,s6,s7,s8]
    inputs = [s1,s2,s3]
    ret = s.insert(inputs,new)
    for i in ret:
        print i.start
        print i.end
