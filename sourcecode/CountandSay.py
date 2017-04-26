class Solution(object):
  def countAndSay(self, n):
    if n <= 0 :
      return ""
    if n == 1:
      return "1"
    x = "1"
    nx = None
    for i in range(1,n):
      nx = "";
      j = 0
      while j < len(x):
        c = x[j]
        cnt = 1
        j += 1
        while j < len(x) and x[j] == c:
          j+=1
          cnt+=1
        nx = nx + str(cnt) + c
      x = nx
    if nx != None and len(nx) > 0:
      x = nx
    return x;

if __name__ == "__main__":
  s = Solution()
  r = s.countAndSay(6)
  print r
