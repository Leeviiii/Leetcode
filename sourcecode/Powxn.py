class Solution(object):
  def myPow(self,x,n):
    if n == 0:
      return 1
    if n < 0:
      return 1.0/self.power(x,-n)
    return self.power(x,n)
  def power(self,x,n):
    if n==0:
      return 1
    v = self.power(x,n/2)
    if n%2 == 0:
      return v*v
    else:
      return v*v*x
    




if __name__ == "__main__":
  s = Solution()
  r = s.myPow(0.00001,2147483647)
  print r
