#! usr/bin/python
#coding=utf-8 
class Solution(object):
	def twoSum(self, nums, target):
		tmp = {}
		i = 0
		#如果num有重复的，那么后面的num下标会被记录
		for num in nums:
			tmp[num] = i
			i+=1
		for i in range(len(nums)):
			num = nums[i]
			num1 = target - num
			if num1 in tmp.keys():
				k1 = tmp[num1]
				#防止出现 [3,5,11] 6的case
				if k1 == i:
					continue;
				return [i,k1]
		return None


if __name__ == "__main__":
	nums = [3,3,5,11]
	s = Solution()
	ret = s.twoSum(nums,6)
	print ret
