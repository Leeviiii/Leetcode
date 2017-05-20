# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p != None and p.next != None:
            if p.val == p.next.val:
                p.next = p.next.next
            else :
                p = p.next
        return head

if __name__ == "__main__":
    s = Solution()
    a1 = ListNode(1)
    a2 = ListNode(1)
    a3 = ListNode(1)
    a1.next = a2;
    a2.next = a3
    r = s.deleteDuplicates(a1)
    while r != None:
        print r.val
        r = r.next
