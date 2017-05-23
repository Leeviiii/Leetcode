## [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/#/description)

Given n non-negative integers representing the histogram bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

## 分析：

解法一：用一个数组存储(i,j)的最小值，然后计算每一个(i,j)的面积，最后取最大。时间复杂度O(n2)的，会超时

解法二：用一个栈存储着单调增的柱子，当出现不单调增的柱子的时候一次计算整个递增的过程。原因是单调增的柱子可以直接取出来一个柱子对应的面积，因为他是单调赠的，所以他的左边是跟他一样高的上一个位置，他的右边可以一直到遍历到的位置。时间复杂度O(n)

### [实现](../sourcecode/LargestRectangleinHistogram.py)
```
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        stack = []
        heights.append(0)
        maxsum = 0
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[len(stack)-1]] > heights[i]:
                tmp = stack.pop(len(stack)-1)
                leftsum = (tmp+1)*heights[tmp] if len(stack) == 0 else (tmp - stack[len(stack)-1])*heights[tmp]
                rightsum = (i - tmp - 1) * heights[tmp]
                if leftsum + rightsum > maxsum:
                    maxsum = leftsum + rightsum
                stack.append(i)
        return maxsum
```
