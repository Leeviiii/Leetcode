## [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/#/description)

>Given a linked list, remove the nth node from the end of list and return its head.

>For example,Given linked list: 1->2->3->4->5, and n = 2.

>After removing the second node from the end, the linked list becomes 1->2->3->5.

## 分析：

这道题的思路有点类似于快慢指针，让一个块指针先走n步骤，然后快慢指针一起遍历剩下的节点。当快指针的next为None的时候，慢指针刚好走到倒数第n个节点的前一个。

### [实现](../sourcecode/RemoveNthNodeFromEndofList.py)
```
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
```
