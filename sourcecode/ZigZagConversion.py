class Solution(object):
  def convert(self, s, numRows):
    if numRows == 0:
      return None
    if numRows == 1:
      return s
    length = len(s)
    flag = 0
    rowelements = 0
    ret = []
    for i in range(numRows):
      ret.append([])
    pos = 0
    f = numRows - 2 
    zigzags = 0
    i = 0
    while i < len(s):
      if flag < numRows:
        ret[pos].append(s[i])
        i+=1
        pos+=1
        flag+=1
      elif flag == numRows:
        pos = f
        if pos == 0:
          flag = 0
          pos = 0
          continue
        ret[pos].append(s[i])
        i+=1
        pos -= 1
        flag += 1
      else:
        if flag == numRows + f:
          flag = 0
          pos = 0
          continue
        ret[pos].append(s[i])
        i+=1
        flag+=1
        pos-= 1

    s1 = '';
    for l in ret:
      for c in l:
        s1 = s1 + c
    return s1

        




if __name__ == "__main__":
  s = Solution()
  r = s.convert("PAYPALISHIRING",4)
  print r
