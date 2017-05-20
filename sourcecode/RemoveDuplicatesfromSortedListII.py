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
        if head == None or head.next == None:
            return head
        p = head
        vmap = {}
        while p != None:
            val = p.val
            vmap[val] = vmap[val] + 1 if (val in vmap) else 1   
            p = p.next
        h1 = None
        q1 = h1
        p = head
        while p != None:
            if vmap[p.val] == 1:
                if h1 == None:
                    h1 = p
                    q1 = h1
                else:
                    q1.next = p
                    q1 = q1.next 
            p = p.next
        if q1 != None:
            q1.next = None
        return h1

if __name__ == "__main__":
    s = Solution()
    a1 = ListNode(1)
    a2 = ListNode(1)
    a3 = ListNode(1)
    a4 = ListNode(1)
    a1.next = a2;
    a2.next = a3
    a3.next = a4
    r = s.deleteDuplicates(a1)
    while r != None:
        print r.val
        r = r.next
