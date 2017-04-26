## [Count and Say](https://leetcode.com/problems/count-and-say/#/description)

>The count-and-say sequence is the sequence of integers beginning as follows:1, 11, 21, 1211, 111221, ...

>1 is read off as "one 1" or 11.

>11 is read off as "two 1s" or 21.

>21 is read off as "one 2, then one 1" or 1211.

>Given an integer n, generate the nth sequence.

>Note: The sequence of integers will be represented as a string.

## 分析：

根据规律写代码就好了

### [实现](../sourcecode/CountandSay.py)
```
class Solution(object):
  def countAndSay(self, n):
    if n <= 0 :
      return ""
    if n == 1:
      return "1"
    x = "1"
    nx = None
    for i in range(1,n):
      nx = "";
      j = 0
      while j < len(x):
        c = x[j]
        cnt = 1
        j += 1
        while j < len(x) and x[j] == c:
          j+=1
          cnt+=1
        nx = nx + str(cnt) + c
      x = nx
    if nx != None and len(nx) > 0:
      x = nx
    return x;
```

