# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def reverseKGroup(self, head, k):
    if k == 1:
      return head
    if k <= 0:
      return head
    l1 = head 
    l2 = head
    l3 = head
    i = 1
    length = 0
    isfirst = 1
    while l2 != None:
      if i < k:
        i += 1
        l2 = l2.next
        length += 1
      else:
        p1 = l1
        p2 = l1.next
        p3 = p2.next
        p4 = l2.next
        for i in range(1,k):
          p2.next = p1
          p1 = p2
          p2 = p3
          if p3 == None:
            break
          p3 = p3.next
        if isfirst == 1:
          head = p1
          isfirst = 0
        else:
          l3.next = p1
        isfirst = 0
        l1.next = p4
        l3 = l1
        l1 = p4;
        l2 = l1
        i = 1
    return head



if __name__ == "__main__":
  s = Solution()
  a = ListNode(1);
  b = ListNode(2);
  c = ListNode(3);
  d = ListNode(4);
  e = ListNode(5);
  a.next = b
  #b.next = c
  c.next = d
  d.next = e

  r = s.reverseKGroup(a,1)
  while r!= None:
    print r.val
    r = r.next
