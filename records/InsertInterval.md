## [Insert Interval](https://leetcode.com/problems/insert-interval/#/description)

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

## 分析：

这道题目实际上是一个二分查找,找到newInterval需要插入的位置，然后就是一个[MergeIntervals.md](./MergeIntervals.md)问题了，比MergeIntervals问题省下了一步排序。二分复杂度O(lgn)，遍历进行merge操作O(n)，所以时间负责度为O(n)

### [实现](../sourcecode/InsertInterval.py)
```
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

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
