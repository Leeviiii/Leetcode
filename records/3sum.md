## [3Sum](https://leetcode.com/problems/3sum/#/description)

>Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

>Note: The solution set must not contain duplicate triplets

## 分析：

排序，然后二重循环扫描，相当于n个2-sum的问题

### [实现](../sourcecode/3sum.py)
```
class Solution(object):
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
```


  
