'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

import sys
sys.path.append("../../datastuctures")
from linkedlist.linkedlist import ListNode

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        p, c = head, head.next
        while c:
            if p.val == c.val:
                p.next = c.next
            else:
                p = c
            c = c.next
        return head

if __name__ == "__main__":
    l1 = ListNode(1)(ListNode(1)(ListNode(2)))
    assert "1,2" == str(Solution().deleteDuplicates(l1))