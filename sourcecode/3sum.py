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
	def threeSum(self, nums):
		if len(nums)<3:
			return []
		ret = []
		self.quicksort(nums,0,len(nums)-1)
		target = 0
		for i in range(len(nums)):
			if i > 0 and nums[i] == nums[i-1]:
				continue;
			twosum = target - nums[i]
			l = i + 1
			r = len(nums) - 1
			while l < r:
				if nums[l] + nums[r] == twosum:
					ret.append([nums[i],nums[l],nums[r]])
					l+=1
					r-=1
					while l < r and nums[r] == nums[r+1] :
						r -= 1
					while l < r and nums[l] == nums[l-1] :
						l += 1
				elif nums[l] + nums[r] > twosum:
					r-=1
					while l < r and nums[r] == nums[r+1] :
						r -= 1
				else:
					l += 1
					while l < r and nums[l] == nums[l-1] :
						l += 1
		return ret


if __name__ == "__main__":
	nums = [-13,5,13,12,-2,-11,-1,12,-3,0,-3,-7,-7,-5,-3,-15,-2,14,14,13,6,-11,-11,5,-15,-14,5,-5,-2,0,3,-8,-10,-7,11,-5,-10,-5,-7,-6,2,5,3,2,7,7,3,-10,-2,2,-12,-11,-1,14,10,-9,-15,-8,-7,-9,7,3,-2,5,11,-13,-15,8,-3,-7,-12,7,5,-2,-6,-3,-10,4,2,-5,14,-3,-1,-10,-3,-14,-4,-3,-7,-4,3,8,14,9,-2,10,11,-10,-4,-15,-9,-1,-1,3,4,1,8,1]
	s = Solution()
	nums = s.threeSum(nums)
	print nums
