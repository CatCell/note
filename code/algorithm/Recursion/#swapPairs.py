# swapPairs
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 这个不算递归吧
        # 链表不是很懂
        start = ListNode(0)
        start.next = head
        curr = start
        while curr.next and curr.next.next:
            node1 = curr.next
            node2 = curr.next.next
            curr.next = node2
            node1.next = node2.next  # 需要和后面链接
            node2.next = node1
            curr = node1
        return start.next
