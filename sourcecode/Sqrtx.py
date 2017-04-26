class Solution(object):
  def mySqrt(self, x):
    if x <= 1:
      return x
    begin = 1
    end = x

    while True:
      m = (begin + end)/2
      t = m*m
      if t == x:
        return m
      if t > x:
        end = m
        t1 = (m-1)*(m-1)
        if t1 < x:
          return m - 1
      else :
        begin = m
        t1 = (m+1)*(m+1)
        if t1 > x:
          return m
if __name__ == "__main__":
  s = Solution()
  r = s.mySqrt(9)
  print r
