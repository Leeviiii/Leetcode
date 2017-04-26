# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def removeNthFromEnd(self, head, n):
    if n <= 0 :
      return head
    if head == None:
      return None
    l1 = head 
    l2 = head
    i = 0
    l = 1
    while l2.next != None:
      l+=1
      if i < n:
        i+=1
        l2 = l2.next
      else:
        l1 = l1.next
        l2 = l2.next
    if i < n :
      head = head.next
      return head
    if l1.next != None:
      l1.next = l1.next.next
    return head
if __name__ == "__main__":
  s = Solution()
  a = ListNode(1);
  b = ListNode(2);
  a.next = b

  r = s.removeNthFromEnd(a,2)
  while r!= None:
    print r.val
    r = r.next
