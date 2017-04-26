# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def mergeTwoLists(self, l1, l2):
    if l1 == None:
      return l2
    if l2 == None:
      return l1
    head = None
    p = None
    while l1 != None and l2 != None:
      if l1.val < l2.val:
        if head == None:
          head = l1
          p = head
        else:
          p.next = l1
          p = p .next
        l1 = l1.next
      else :
        if head == None:
          head = l2
          p = head
        else:
          p.next = l2
          p = p .next
        l2 = l2.next
    if l1 != None:
      p.next = l1
    elif l2 != None:
      p.next = l2
    else:
      p.next = None
    return head
if __name__ == "__main__":
  s = Solution()
  a = ListNode(1);
  b = ListNode(2);
  c = ListNode(2);
  a1 = ListNode(1);
  b1 = ListNode(1);
  c1 = ListNode(2);
  #a.next = b
  #b.next = c
  #a1.next = b1
  #b1.next = c1

  r = s.mergeTwoLists(a,b)
  while r!= None:
    print r.val
    r = r.next
