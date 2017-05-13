## [Rotate Image](https://leetcode.com/problems/rotate-image/#/description)


>You are given an n x n 2D matrix representing an image.

>Rotate the image by 90 degrees (clockwise).

>Could you do this in-place?

## 分析：

原地顺时针旋转90度，题目就是基本的数组操作，写起来在逻辑上其实有一点难度。我的方法是以某一个点为中心，一层一层的选择，但是要分为奇偶两种情况，下面以偶数为例，偶数要复杂一下。

-------------------------------->x
|
|
|      -----------------
|      |               |
|      |               |
|      |      ..       |
|      |      ..       |
|      |               |
|      |               |
|      |---------------|
|
V
y

上图的横轴是x轴，纵轴是y轴，因为是偶数所以中心是一个2*2的小正方形，按照层次旋转就是先旋转0层的就最中间的四个点，在选择1层的，即最中间外面第一层的12个点，一直循环到最外一层就完成了90度的选择。这里只要梳理清理角落四个点的坐标就可以，这里假设中心点放生在x=centerl，x=centerr这两个位置上，那么在第level层，可以得到

```
左上点坐标(centerl-level,centerl-level)
右上点坐标(centerr+level,centerl-level)
坐下点坐标(centerl-level,centerr+level)
右下点坐标(centerr+level,centerr+level)
```

梳理好上面的四个点，然后一次从centerl-level遍历到centerr+level就可以旋转玩一层了。

### [实现](../sourcecode/RotateImage.py)
```
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)%2 == 1:
            center = len(matrix)/2
            for level in range(center+1):
                self.rotateOneLevel1(matrix,level,center)
            else:
                centerl = len(matrix)/2 - 1
                centerr = len(matrix)/2
                for level in range(centerr):
                    self.rotateOneLevel2(matrix,level,centerl,centerr)

    def rotateOneLevel1(self, matrix, level, center):
        if level == 0:
            return
        for i in range(center-level,center + level):
            d = i - (center-level)
            tmp = matrix[center-level][i]
            matrix[center-level][i] = matrix[center+level-d][center-level]
            matrix[center+level-d][center-level] = matrix[center+level][center+level-d]
            matrix[center+level][center+level-d] =  matrix[center-level+d][center+level]
            matrix[center-level+d][center+level] = tmp


    def rotateOneLevel2(self, matrix, level, centerl, centerr):
        for i in range(centerl-level,centerr+level):
            d = i - (centerl-level)
            tmp = matrix[centerl-level][i]
            matrix[centerl-level][i] = matrix[centerr+level-d][centerl-level] 
            matrix[centerr+level-d][centerl-level] = matrix[centerr+level][centerr+level-d]
            matrix[centerr+level][centerr+level-d] = matrix[centerl-level+d][centerr+level]
            matrix[centerl-level+d][centerr+level] = tmp
```
