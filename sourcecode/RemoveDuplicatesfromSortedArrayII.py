class Solution(object):
  def removeDuplicates(self, nums):
    l1 = 0
    l2 = 1
    dup = 0
    if len(nums) > 0:
      lastn = nums[0]
    nums_du = {}
    n = 0
    for i in range(len(nums)):
        if i != n:
            nums[n] = nums[i]
        if nums[i] in nums_du:
            cnt = nums_du[nums[i]]
            if cnt == 1:
                n += 1
            nums_du[nums[i]] += 1
        else:
            nums_du[nums[i]] = 1
            n += 1
    return n

if __name__ == "__main__":
  s = Solution()
  r = s.removeDuplicates([1,1,1,2,2])
  print r
