#! usr/bin/python
#coding=utf-8 
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		if len(s) <= 1:
			return len(s)
		index = {}
		index[s[0]] = 0
		begin = 0
		end = 0
		maxbegin = 0
		maxend = 0;
		for i in range(1,len(s)):
			c = s[i]
			if c not in index:
				index[c] = i
				end += 1
				continue
			p = index[c]
			if p >= begin and p <= end:
				if maxend - maxbegin < end - begin:
					maxend = end
					maxbegin = begin;
				begin = p + 1
				end = i
			else:
				end+=1
			index[c] = i
		if end > len(s) - 1:
			end = len(s) - 1
		if maxend - maxbegin < end - begin:
			maxend = end
			maxbegin = begin;
		return maxend - maxbegin + 1


			



if __name__ == "__main__":
	s = Solution()
	s1 = "qwnfenpglqdq"
	t = s.lengthOfLongestSubstring(s1)
	print t
