class Solution(object):
  def search(self, nums, target):
    if len(nums) == 0:
      return -1
    begin = 0
    end = len(nums) - 1
    return self.binarysearch(nums,begin,end,target)
  def binarysearch(self,nums,begin,end,target):
    if end == begin:
      if nums[begin] == target:
        return begin
      return -1
    if end - begin == 1:
      if nums[begin] == target:
        return begin
      if nums[end] == target:
        return end
      return -1
    m = (begin + end)/2
    if nums[m] == target:
      return m
    if nums[m] < nums[begin] and nums[m] < nums[end]:
      if target > nums[m]:
        x = self.binarysearch(nums,begin,m,target)
        if x == -1:
          return self.binarysearch(nums,m,end,target)
        return x
      else:
        return self.binarysearch(nums,begin,m,target)
    else:
      if target > nums[m]:
        return self.binarysearch(nums,m,end,target)
      else:
        x = self.binarysearch(nums,begin,m,target)
        if x == -1:
          return self.binarysearch(nums,m,end,target)
        return x




if __name__ == "__main__":
  s = Solution()
  nums  = [6,7,1,2,3,4,5] 
  #nums  = [5,1,2,3,4] 
  #nums  = [3,1] 
  r = s.search(nums,6)
  print r
