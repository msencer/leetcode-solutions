'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

import sys
sys.path.append("../../datastuctures")
from linkedlist.linkedlist import ListNode

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return

        nth = head
        i = 0
        while nth.next and i < n:
            nth = nth.next
            i += 1

        if i == n - 1:
            return head.next
        elif i < n:
            return

        cur = head

        while nth.next:
            cur = cur.next
            nth = nth.next

        if cur.next.next:
            cur.next.val = cur.next.next.val
            cur.next = cur.next.next
        else:
            cur.next = None

        return head

if __name__ == "__main__":
    l1 = ListNode(1)(ListNode(1)(ListNode(2)))
    assert "1,1" == str(Solution().removeNthFromEnd(l1,1))
    assert "1,2" == str(Solution().removeNthFromEnd(l1, 2))