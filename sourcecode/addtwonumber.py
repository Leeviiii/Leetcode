#! usr/bin/python
#coding=utf-8 
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution(object):
	def addTwoNumbers(self, l1, l2):
		isaddone = 0
		ret = None
		head = None
		while l1 != None and l2 != None:
			sumt = l1.val + l2.val + isaddone
			if isaddone == 1:
				isaddone = 0
			if sumt > 9:
				isaddone = 1
				sumt = sumt - 10
			if ret == None:
				ret = ListNode(sumt)
				head = ret
			else:
				ret.next = ListNode(sumt)
				ret = ret.next
			l1 = l1.next
			l2 = l2.next
		while l1 != None:
			sumt = l1.val + isaddone
			if isaddone == 1:
				isaddone = 0
			if sumt > 9:
				isaddone = 1
				sumt = sumt - 10
			ret.next = ListNode(sumt)
			ret = ret.next
			l1 = l1.next
		while l2 != None:
			sumt = l2.val + isaddone
			if isaddone == 1:
				isaddone = 0
			if sumt > 9:
				isaddone = 1
				sumt = sumt - 10
			ret.next = ListNode(sumt)
			ret = ret.next
			l2 = l2.next
		if isaddone == 1:
			ret.next = ListNode(1)
		return head



if __name__ == "__main__":
	s = Solution()
	l1 = ListNode(9)
	l1.next = ListNode(9)
	#l1.next.next = ListNode(3)
	l2 = ListNode(9)
	#l2.next = ListNode(6)
	#l2.next.next = ListNode(4)
	r = s.addTwoNumbers(l1,l2)
	while r != None:
		print r.val
		r = r.next
