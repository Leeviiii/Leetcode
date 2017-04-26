class Solution(object):
  def findMin(self, nums):
    if len(nums) == 0:
      return None
    if len(nums) == 1:
      return nums[0]
    begin = 0
    end = len(nums) - 1
    if nums[end] > nums[0]:
      return nums[0]
    while True:
      if end - begin == 1:
        return min(nums[begin],nums[begin + 1])
      m = (begin + end)/2
      if nums[m] < nums[m - 1] and nums[m] < nums[m + 1]:
        return nums[m]
      if nums[m] < nums[begin] and nums[m] < nums[end]:
        end = m
      else :
        begin = m


if __name__ == "__main__":
  s = Solution()
  #nums  = [4,5,6,7,8,9,1,2,3] 
  #nums  = [5,1,2,3,4] 
  nums  = [3,1] 
  r = s.findMin(nums)
  print r
