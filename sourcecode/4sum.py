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
	def fourSum(self, nums,target):
		if len(nums)<4:
			return []
		ret = []
		self.quicksort(nums,0,len(nums)-1)
		for k in range(len(nums)):
			threesum = target - nums[k]
			if k > 0 and nums[k] == nums[k-1]:
				continue;
			for i in range(k+1,len(nums)):
				if i > k+1 and nums[i] == nums[i-1]:
					continue;
				twosum = threesum- nums[i]
				l = i + 1
				r = len(nums) - 1
				while l < r:
					if nums[l] + nums[r] == twosum:
						ret.append([nums[k],nums[i],nums[l],nums[r]])
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
	nums = [-1,0,1,2,-1,-4]
	s = Solution()
	nums = s.fourSum(nums,-1)
	print nums
