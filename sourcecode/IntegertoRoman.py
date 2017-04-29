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



        




if __name__ == "__main__":
    s = Solution()
    r = s.intToRoman(3999)
    print r
