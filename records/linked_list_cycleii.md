## [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/#/description)

>Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

>Note: Do not modify the linked list.

>Follow up:Can you solve it without using extra space?

## 分析：

题目要求是不允许使用额外的空间，那么如果允许呢？
>如果允许使用额外空间，直接使用hash表存储每一个节点，然后遍历链表就可以，需要O(n)的空间，时间复杂度也是O(n)

如果不允许额外的空间，就使用快慢指针来解决就可以了。我们假设一个有环链表如下结构:
```
n1->n2->...nk->c1->c2->...ci->nk
|<----k----->|<-----i-------|
```
这里假设环的长度为i，头到环入口节点的距离为k，快慢指针相遇的节点距离c1为l。快指针走的距离一定为慢指针的两倍，所以:
>(k+l+m*i) = 2(k+l)    m是快指针走的圈数

>因此可以得到公式mi = k + l ,再推倒一步就是(m-1)*i + i - l = k

>k是从头到环入口走过的长度,i-l刚好是从相遇点走到环入口的长度，他们的差刚好是环的整数或者0倍。

>因此让一个指针指向头，一个指针指向相遇点，这两个指针一起走，一定在入口处相遇。

可以看到nk就是环的开始节点
### [实现](../sourcecode/LinkedListCycleII.py)
```
class Solution(object):
  def detectCycle(self, head):
    if head == None:
      return None
    l1 = head
    l2 = head
    while l1 != None and l2 != None:
      l1 = l1.next
      l2 = l2.next
      if l2 != None:
        l2 = l2.next
      else :
        break
      if l1 == l2 :
        l3 = head
        while l3 != l2 :
          l2 = l2.next
          l3 = l3.next
        return l2
    return None

```
