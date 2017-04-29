## [Integer to Roman](https://leetcode.com/problems/integer-to-roman/#/description)

>Given an integer, convert it to a roman numeral.Input is guaranteed to be within the range from 1 to 3999.


## 分析：

做好对应关系就可以。

PS:查了一下罗马数字的表示方法，感觉每个人说的都不太一样，奇葩。

### [实现](../sourcecode/IntegertoRoman.py)
```
class Solution(object):
    def intToRoman(self, num):
        int_roman = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}        
        numlist = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman = ""
        for j in range(len(numlist)):
            k = numlist[j]
            c = int_roman[k]
            while num >= k:
                roman = roman + c
                num -= k
        return roman
```


  
