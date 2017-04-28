## [Palindrome Number](https://leetcode.com/problems/palindrome-number/#/description)

>Determine whether an integer is a palindrome. Do this without extra space.

## 分析：

将原来的数组旋转，然后跟原来的进行比较，相等就是回文整数，否则就不是

### [实现](../sourcecode/PalindromeNumber.py)
```
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        y = 0
        s = x
        while True:
            if x == 0:
                break
            t = x%10
            y = y*10 + t
            x = x/10
        if s == y:
            return True
        return False
```
