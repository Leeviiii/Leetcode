## [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/#/description)

>Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

## 分析：

k路归并，二二归并，采用二分思想，这样的好处的小的先合并，然后变成大的再合并

### [实现](../sourcecode/MergekSortedLists.py)
```
class Solution(object):
  def mergeKLists(self, lists):
    k = len(lists)
    if k == 0:
      return []
    if k == 1:
      return lists[0]
    return self.mergerecur(lists, 0, len(lists) - 1)
  def mergerecur(self, lists, start, end):
    if start == end:
      return lists[start]
    mid = (start+end)/2
    left = self.mergerecur(lists,start,mid)
    right = self.mergerecur(lists,mid + 1,end)
    return self.mergeTwoLists(left, right)
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
