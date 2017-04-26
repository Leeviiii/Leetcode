## [Reverse Integer](https://leetcode.com/problems/reverse-integer/#/description)

>Reverse digits of an integer.

>Example1: x = 123, return 321

>Example2: x = -123, return -321

## 分析：

这种类型的题目不知道改怎么分类，不是正常的数据结构题目，觉得就是正常的思考逻辑题目。这个题目就是用过除10模10两种操作就可以得到答案了。

### [实现](../sourcecode/ReverseInteger.py)
```
class Solution(object):
  def reverse(self, x):
    min_int = -2147483646
    max_int = 2147483647
    y = 0
    i = 10 
    j = 0
    if x < 0:
      x = -x
      flag = 1
    else :
      flag = 0
    while True:
      if x == 0:
        break
      t = x%10
      y = y*10 + t
      x = x/10
      if flag == 1:
        y = -y
      if y > max_int or y < min_int:
        return 0 
    return y
```
