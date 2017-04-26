## [3Sum Closest](https://leetcode.com/problems/3sum-closest/#/description)

>Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

## 分析：

排序

### [实现](../sourcecode/3sum_closest.md)
```
class Solution(object):
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
```
