class Solution(object):
    def romanToInt(self, s):
        roman_int = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}        
        slist = ['M','D','C','L','X','V','I']
        slist2 = ['CM','CD','XC','XL','IX','IV']
        num = 0
        i = 0
        while i < len(s):
            if i != len(s) -1 :
                c = s[i:i+2]
                if c in roman_int:
                    num += roman_int[c]
                    i += 2
                    continue;
            c = s[i]
            i+=1
            num += roman_int[c]

        return num



        




if __name__ == "__main__":
    s = Solution()
    r = s.romanToInt("MMMCMXCIX")
    print r
