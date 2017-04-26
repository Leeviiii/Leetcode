#! usr/bin/python
#coding=utf-8 
class Solution(object):
	def quicksort(self,nums,begin,end):
		if begin >= end:
			return
		if end - begin + 1 <= 7 :
			self.insertsort(nums,begin,end);
			return
		l = self.partiton(nums,begin,end);
		self.quicksort(nums,0,l-1);
		self.quicksort(nums,l+1,end);
	def insertsort(self, nums, begin, end):
		for i in range(begin + 1, end + 1):
			for j in range(begin, i):
				if nums[j] > nums[i]:
					tmp = nums[i]
					nums[i] = nums[j]
					nums[j] = tmp
	def partiton(self,nums,begin,end):
		midvalue = nums[end];
		l = begin;
		r = end - 1
		while l <= r:
			if nums[l] < midvalue:
				l += 1
				continue
			tmp = nums[r]
			nums[r] = nums[l]
			nums[l] = tmp
			r -= 1
		nums[end] = nums[l]
		nums[l] = midvalue
		return l
	def threeSumClosest(self, nums, target):
		if len(nums)<3:
			return []
		ret = []
		self.quicksort(nums,0,len(nums)-1)
		current_diff = 0;
		for i in range(len(nums)):
			twosum = target - nums[i]
			l = i + 1
			r = len(nums) - 1
			while l < r:
				tmpsum = nums[l] + nums[r]
				if tmpsum == twosum:
					ret = [nums[i],nums[l],nums[r]]
					current_diff = 0
					break;	
				elif tmpsum > twosum:
					diff = tmpsum - twosum
					if current_diff == 0 or current_diff > diff :
						ret = [nums[i],nums[l],nums[r]]
						current_diff = diff
					r -= 1
				else :
					diff = twosum -tmpsum 
					if current_diff == 0 or current_diff > diff :
						ret = [nums[i],nums[l],nums[r]]
						current_diff = diff
					l += 1
			if current_diff == 0:
				break
		return ret[0] + ret[1] +ret[2]


if __name__ == "__main__":
	nums = [4,-1,-4,4];
	target = -1
	s = Solution()
	nums = s.threeSumClosest(nums,target)
	print nums
