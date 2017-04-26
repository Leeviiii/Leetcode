## [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/#/description)

>Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

## 分析：

二路归并，时间复杂度O(m+n)

### [实现](../sourcecode/MergeTwoSortedLists.py)
```
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
```
