## [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/#/description)

>Given a linked list, determine if it has a cycle in it.

>Follow up:Can you solve it without using extra space?

## 分析：

题目要求是不允许使用额外的空间，那么如果允许呢？
>如果允许使用额外空间，直接使用hash表存储每一个节点，然后遍历链表就可以，需要O(n)的空间，时间复杂度也是O(n)

如果不允许额外的空间，就使用快慢指针来解决就可以了。如果有环，快慢指针必定相遇。
### [实现](../sourcecode/LinkedListCycle.py)
```
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
```
