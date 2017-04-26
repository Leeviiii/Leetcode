## [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/#/description)

>Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

>k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

>You may not alter the values in the nodes, only nodes itself may be changed.

>Only constant memory is allowed.

>Given this linked list: 1->2->3->4->5

>For k = 2, you should return: 2->1->4->3->5

>For k = 3, you should return: 3->2->1->4->5

## 分析：

这应该算是一道很复杂的链表操作题目了，想要完成在某一个位置对前面一段节点进行翻转至少需要三个指针
>一个指向需要翻转开始的开始节点代码中的l1,一个指向需要旋转的结束节点如下面的l2，一个指向l2的next，用来做旋转

>还有两个地方需要考虑，一个是第一次旋转的时候要把head指向新的正确的head；每一次旋转结束后，想把旋转的组跟前面的连起来，最后一个旋转需要把旋转组跟最后一组无法旋转的节点连起来

### [实现](../sourcecode/ReverseNodesink-Group.py)
```
class Solution(object):
  def reverseKGroup(self, head, k):
    if k == 1:
      return head
    if k <= 0:
      return head
    l1 = head 
    l2 = head
    l3 = head
    i = 1
    length = 0
    isfirst = 1
    while l2 != None:
      if i < k:
        i += 1
        l2 = l2.next
        length += 1
      else:
        p1 = l1
        p2 = l1.next
        p3 = p2.next
        p4 = l2.next
        for i in range(1,k):
          p2.next = p1
          p1 = p2
          p2 = p3
          if p3 == None:
            break
          p3 = p3.next
        if isfirst == 1:
          head = p1
          isfirst = 0
        else:
          l3.next = p1
        isfirst = 0
        l1.next = p4
        l3 = l1
        l1 = p4;
        l2 = l1
        i = 1
    return head
```
