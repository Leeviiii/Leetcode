## Sqrt(x) 

>Implement int sqrt(int x).
>Compute and return the square root of x.

[原题地址](https://leetcode.com/problems/sqrtx/#/description)


## 分析：
主意上面的sqrt函数返回值是int，所以比正常的sqrt要简单的多。

- 解法一：暴力遍历，1到x直接的所有可能值，时间复杂度O(n)
- 解法二：对1到x之间的所有值显然是有序而且没有重复的，可以进行二分查找，时间复杂度O(lgn)

### 非递归实现
```
class Solution(object):
  def mySqrt(self, x):
    if x <= 1:
      return x
    m = (1+x)/2
    t = m*m
    begin = 1
    end = x
    while True:
      if t == x:
        return m
      if t > x:
        end = m
        t1 = (m-1)*(m-1)
        if t1 < x:
          return m - 1
      else :
        begin = m
        t1 = (m+1)*(m+1)
        if t1 > x:
          return m
      m = (begin + end)/2
      t = m*m 
```
### 递归实现
```
class Solution(object):
  def mySqrt(self, x):
    if x <= 1:
      return x
    return self.sqrt_r(x, 1, x)
  def sqrt_r(self, x , begin, end):
    m = (begin + end)/2
    t = m*m
    if t == x:
      return m
    elif t > x:
      if (m-1)*(m-1) < x:
        return m - 1
      return self.sqrt_r(x, begin, m)
    else:
      if (m+1)*(m+1) > x:
        return m
      return self.sqrt_r(x, m, end)
```

