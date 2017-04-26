class Solution(object):
  def search(self, nums, target):
    if len(nums) == 0:
      return False
    for i in range(len(nums)):
      if nums[i] == target:
        return True
    return False



if __name__ == "__main__":
  s = Solution()
  nums  = [6,7,1,2,3,4,5] 
  #nums  = [5,1,2,3,4] 
  #nums  = [3,1] 
  r = s.search(nums,6)
  print r
