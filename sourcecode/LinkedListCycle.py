# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  def __str__(self):
    return "val is %d " % self.val

class Solution(object):
  def hasCycle(self, head):
    if head == None:
      return False
    l1 = head
    l2 = head.next
    while l1 != None and l2 != None:
      if l1 == l2 :
        return True
      l1 = l1.next
      l2 = l2.next
      if l2 != None:
        l2 = l2.next
      else :
        break
    return False



if __name__ == "__main__":
  s = Solution()
  a = ListNode(1);
  b = ListNode(2);
  c = ListNode(3);
  d = ListNode(4);
  e = ListNode(5);
  a.next = b
  b.next = c
  c.next = d
  d.next = e
  e.next = a

  r = s.hasCycle(a)
  print r
