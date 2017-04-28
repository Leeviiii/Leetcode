#! usr/bin/python
#coding=utf-8 
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

if __name__ == "__main__":
	nums = 123321
	s = Solution()
	ret = s.isPalindrome(nums)
	print ret
