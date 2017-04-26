## [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/#/description)

>Implement atoi to convert a string to an integer.

## 分析：

考虑好所有的special input。

### [实现](../sourcecode/atoi.py)
```
class Solution(object):
  def myAtoi(self, str):
    min_int = -2147483648
    max_int = 2147483647
    maptable = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9};
    if len(str) == 0:
      return 0
    for i in range(len(str)):
      if str[i] != ' ':
        break;
    x = 0
    flag = 0
    if i == len(str):
      return 0 
    if str[i] == '+':
      flag = 1
    if str[i] == '-':
      flag = 2
    if flag != 0:
      i += 1
    for j in range(i,len(str)):
      if str[j] in maptable:
        n = maptable[str[j]]
        x = 10*x + n
      else:
        break;
    if flag == 2:
      x = -x
    if x > max_int:
      x = max_int
    if x < min_int:
      x = min_int
    return x
```
