# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "start is %d,end is %d" % (self.start,self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals,key=lambda i: i.start)
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
    s1 = Interval(5,5)
    s2 = Interval(2,4)
    s3 = Interval(4,6)
    s4 = Interval(3,4)
    s5 = Interval(0,0)
    s6 = Interval(1,1)
    s7 = Interval(3,5)
    s8 = Interval(2,2)
    inputs = [s1,s2,s3,s4,s5,s6,s7,s8]
    ret = s.merge(inputs)
    for i in ret:
        print i.start
        print i.end
