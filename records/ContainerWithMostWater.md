## [Container With Most Water](https://leetcode.com/problems/container-with-most-water/#/description)

>Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

## 分析：

- 解法一：直接暴力循环，两重循环遍历所有的可能，取最大值，时间复杂度O(n*n)。[代码实现](../sourcecode/ContainerWithMostWater.py)
- 解法一：思考一下暴力循环的时候有没有不需要的计算?蓄水的多少取决于短板，所以如果一个大范围的蓄水值被算出来，那么以短板为一边边界的小范围值就不用计算了，肯定不是最优解，这就是贪心的思想。如果我们算出来i-->j的蓄水值，并且ai<aj,那么i-->i+1,i-->i+2......i-->j-1都不需要计算了，一定比i-->j的蓄水值要小。这种方法两边遍历，一次就可以得出结果，时间复杂度O(n)

### [实现](../sourcecode/ContainerWithMostWaterv2.py)
```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        begin = 0
        end = len(height) - 1
        maxv = 0
        while begin < end:
            v = (end - begin)*min(height[begin],height[end])
            maxv = max(v,maxv)
            if height[begin] < height[end]:
                begin += 1
            else:
                end -= 1

        return maxv
```
