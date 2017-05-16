## [Merge Intervals](https://leetcode.com/problems/merge-intervals/#/description)

>Given a collection of intervals, merge all overlapping intervals.

## 分析：

按照start排序后，按照end进行合并，涉及到排序所以时间复杂度O(nlgn)

### [实现](../sourcecode/MergeIntervals.py)
```
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

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

```                                                                                                                                                                                                                                                                                                                                                          
