class Solution(object):
  def isPerfectSquare(self, x):
    if x <= 1:
      return True
    begin = 1
    end = x
    while True:
      m = (begin+end)/2
      t = m*m
      if t == x:
        return True
      if t > x:
        end = m
        t1 = (m-1)*(m-1)
        if t1 < x:
          return False
      else :
        begin = m
        t1 = (m+1)*(m+1)
        if t1 > x:
          return False




if __name__ == "__main__":
  s = Solution()
  r = s.isPerfectSquare(122)
  print r
