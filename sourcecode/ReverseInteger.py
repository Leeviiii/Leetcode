#! usr/bin/python
#coding=utf-8 
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

if __name__ == "__main__":
	nums = 1
	s = Solution()
	ret = s.reverse(nums)
	print ret
