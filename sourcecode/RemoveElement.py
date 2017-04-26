class Solution(object):
  def removeElement(self, nums, val):
    l = 0
    r = len(nums) -1
    dup = 0
    while l <= r:
      n = nums[l]
      if n == val:
        nums[l] = nums[r]
        nums[r] = n
        dup += 1
        r -= 1
      else:
        l += 1
    return len(nums) - dup

        




if __name__ == "__main__":
  s = Solution()
  r = s.removeElement([3,2,2,3],3)
  print r
