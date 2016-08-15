'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''
import sys
sys.path.append("../../datastuctures")
from linkedlist.linkedlist import ListNode

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        c = dummy
        while c.next and c.next.next:
            t1 = c
            c = c.next
            t1.next = c.next

            t2 = c.next.next
            c.next.next = c
            c.next = t2
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1)(ListNode(2)(ListNode(3))(ListNode(4)))
    assert "2,1,4,3" == str(Solution().swapPairs(l1))