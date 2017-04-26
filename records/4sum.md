## [4Sum](https://leetcode.com/problems/4sum/#/description)

>Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

>Note: The solution set must not contain duplicate quadruplets.

## 分析：

排序，然后三重循环扫描，相当于n个3-sum的问题

### [实现](../sourcecode/4sum.py)
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


  
