## [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/#/description)

>Given a positive integer num, write a function which returns True if num is a perfect square else False.

## 分析：
与sqrt思路一致，二分遍历查找就可以

### [实现](../sourcecode/ValidPerfectSquare.py)

```
class Solution(object):
  def isPerfectSquare(self, x):
    if x <= 1:
      return True
    begin = 1
    end = x
    while True:
      m = (begin+end)/2
      t = m*m
      if t == x:
        return True
      if t > x:
        end = m
        t1 = (m-1)*(m-1)
        if t1 < x:
          return False
      else :
        begin = m
        t1 = (m+1)*(m+1)
        if t1 > x:
          return False

```

