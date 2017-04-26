## [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/#/description)

>You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

>You may assume the two numbers do not contain any leading zero, except the number 0 itself.

>Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
>Output: 7 -> 0 -> 8

## 分析：

把一个数字表示为一个链表，对好位置，注意进位就可以了

如果不允许额外的空间，就使用快慢指针来解决就可以了。如果有环，快慢指针必定相遇。
### [实现](../sourcecode/addtwonumber.py)
```
class Solution(object):
  def addTwoNumbers(self, l1, l2):
    isaddone = 0
    ret = None
    head = None
    while l1 != None and l2 != None:
      sumt = l1.val + l2.val + isaddone
      if isaddone == 1:
        isaddone = 0
      if sumt > 9:
        isaddone = 1
        sumt = sumt - 10
      if ret == None:
        ret = ListNode(sumt)
        head = ret
      else:
        ret.next = ListNode(sumt)
        ret = ret.next
      l1 = l1.next
      l2 = l2.next
    while l1 != None:
      sumt = l1.val + isaddone
      if isaddone == 1:
        isaddone = 0
      if sumt > 9:
        isaddone = 1
        sumt = sumt - 10
      ret.next = ListNode(sumt)
      ret = ret.next
      l1 = l1.next
    while l2 != None:
      sumt = l2.val + isaddone
      if isaddone == 1:
        isaddone = 0
      if sumt > 9:
        isaddone = 1
        sumt = sumt - 10
      ret.next = ListNode(sumt)
      ret = ret.next
      l2 = l2.next
    if isaddone == 1:
      ret.next = ListNode(1)
    return head
```

