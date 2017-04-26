class Solution(object):
  def findMin(self, nums):
    if len(nums) == 0:
      return None
    if len(nums) == 1:
      return nums[0]
    minn = nums[0]
    for i in range(1,len(nums)):
      if minn > nums[i] :
        minn = nums[i]
    return minn


if __name__ == "__main__":
  s = Solution()
  #nums  = [4,5,6,7,8,9,1,2,3] 
  #nums  = [5,1,2,3,4] 
  nums  = [10,1,10,10,10,10] 
  r = s.findMin(nums)
  print r
