class Solution(object):
  def removeDuplicates(self, nums):
    l1 = 0
    l2 = 1
    dup = 0
    if len(nums) > 0:
      lastn = nums[0]
    r = len(nums)
    while l2 < r:
      n = nums[l2]
      if n <= lastn:
        l2 += 1
        dup += 1
      else:
        if l2 - l1 > 1:
          nums[l2] = lastn
          nums[l1 + 1] = n
        l1 += 1
        l2 += 1
        lastn = n
    print nums
    return len(nums) - dup

        




if __name__ == "__main__":
  s = Solution()
  r = s.removeDuplicates([1,1,2,3])
  print r
