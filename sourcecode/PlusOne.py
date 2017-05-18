class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == None:
            return [1]
        isadd = 0
        loop = len(digits) - 1
        while loop >= 0:
            n = digits[loop]
            if loop == len(digits) - 1:
                nt = n + isadd + 1
            else:
                nt = n + isadd
            if nt < 10:
                digits[loop] = nt
                isadd = 0
                break
            digits[loop] = nt - 10
            isadd = 1
            loop -= 1
        if isadd == 1:
            digits.insert(0,1)
        return digits
                                                        


                                                            
if __name__ == "__main__":
    s = Solution()
    a = [8,9,9,9]
    print s.plusOne(a)

