## [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/#/description)

>Divide two integers without using multiplication, division and mod operator.

>If it is overflow, return MAX_INT.

## 分析：

这道题的其实不是标准的二分，但是我还是认为这是一个二分的想法。我们用不停地用左移操作逼近结果。

### [实现](../sourcecode/DivideTwoIntegers.py)
```
class Solution(object):
  def divide(self, dividend, divisor):
    if divisor == 0:
      return 0
    min_int = -2147483648
    max_int = 2147483647
    if dividend > max_int or divisor > max_int or dividend<min_int or divisor< min_int:
      return max_int
    if divisor == 1:
      return dividend
    if divisor == -1:
      ret = -dividend
      if ret > max_int:
        return max_int
      return ret
    flag = 0
    if dividend < 0 and divisor < 0:
      dividend = -dividend
      divisor = -divisor
    elif dividend < 0 and divisor > 0:
      dividend = -dividend
      flag = 1
    elif dividend > 0 and divisor < 0:
      divisor = -divisor
      flag = 1 
    else:
      pass
    if dividend < divisor:
      return 0
    r = 0
    v = divisor
    while dividend >= divisor:
      v = divisor
      lastvalue = 0
      ret = 1
      lastret = 0
      while v <= dividend:
        lastret = ret
        lastv = v
        ret = ret << 1
        v = v << 1
      r += lastret
      dividend = dividend - lastv
    if flag == 1:
      r = -r
    return r
```
