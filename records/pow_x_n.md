## [Pow(x, n)](https://leetcode.com/problems/powx-n/#/description)

>Implement pow(x, n).

## 分析：
使用二分法解决

### [实现](../sourcecode/Powxn.py)
```
class Solution(object):
  def myPow(self,x,n):
    if n == 0:
      return 1
    if n < 0:
      return 1.0/self.power(x,-n)
    return self.power(x,n)
  def power(self,x,n):
    if n==0:
      return 1
    v = self.power(x,n/2)
    if n%2 == 0:
      return v*v
    else:
      return v*v*x

```
