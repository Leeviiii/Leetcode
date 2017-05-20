## [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/#/description)

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,

Given 1->2->3->3->4->4->5, return 1->2->5.

Given 1->1->1->2->3, return 2->3.

## 分析：

基本思路不难，直接一个hashmap存储所有的val以及出现的次数，然后只有出现次数为1的节点才保存，其余删除就可以了。但是这样的做法没有用到有序这个条件。所以理论上应该可以不使用hashmap直接做链表处理的，写了写感觉不太好区分[1,2,2,3]和[1,2,2,2]这两种情况，所以就还是使用hashmap accept的了。

### [实现](../sourcecode/RemoveDuplicatesfromSortedListII.py)
```
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
```
