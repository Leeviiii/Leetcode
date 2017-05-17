# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "val is %d " % self.val
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        length = 0
        while p1 != None:
            p1 = p1.next;
            length += 1
        if length == 0 :
            return head
        k = k%length
        p1 = head 
        i = 0
        while i < k:
            i += 1
            if p2 == None:
                return head
            p2 = p2.next
        if p2 == None:
            return head
        while p2.next != None:
            p2 = p2.next
            p1 = p1.next
        p2.next = head
        head = p1.next
        p1.next = None
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
  #c.next = d
  #d.next = e

  r = s.rotateRight(a,3)
  while r != None:
      print r
      r= r.next
