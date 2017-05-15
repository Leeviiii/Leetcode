## [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/#/description)


>Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

## 分析：

什么样子的数据才能装下雨水呢？应该是先一段单调递减，紧接着一个单调递增，这样形成的一个凹陷就可以进行装载的作用，能装多少取决于左右两边最大值的短板。

实现的时候，对数组进行两次扫描，第一次从左到右，扫描出一个位置的左边最大值，然后从右扫描，一边算出右边最大值，一边进行容量计算。每一列一列的计算。

### [实现](../sourcecode/RotateImage.py)
```
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxheight = 0
        leftmax = []
        for i in range(len(height)):
            leftmax.append(maxheight)
            maxheight = max(maxheight,height[i])
        i = len(height) - 1
        maxheight = 0
        t = 0
        while i >= 0:
            tmpmax = min(maxheight,leftmax[i])
            maxheight = max(maxheight,height[i])
            if tmpmax > height[i]:
                t += tmpmax - height[i]
            else:
                pass
            i -= 1
        return t
```
