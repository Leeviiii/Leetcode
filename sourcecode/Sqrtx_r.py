class Solution(object):
  #递归实现
  def mySqrt(self, x):
    if x <= 1:
      return x
    return self.sqrt_r(x, 1, x)
  def sqrt_r(self, x , begin, end):
    m = (begin + end)/2
    t = m*m
    if t == x:
      return m
    elif t > x:
      if (m-1)*(m-1) < x:
        return m - 1
      return self.sqrt_r(x, begin, m)
    else:
      if (m+1)*(m+1) > x:
        return m
      return self.sqrt_r(x, m, end)

if __name__ == "__main__":
  s = Solution()
  r = s.mySqrt(9)
  print r
