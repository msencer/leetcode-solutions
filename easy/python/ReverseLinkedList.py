'''
Reverse a singly linked list.
'''
import sys
sys.path.append("../../datastuctures")
from linkedlist.linkedlist import ListNode
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        c = head
        n = c.next
        while n:
            t = n.next
            n.next = c
            c=n
            n=t
        head.next = None
        return c
if __name__ == "__main__":
    l1 = ListNode(1)(ListNode(2)(ListNode(3)))
    assert "3,2,1" == str(Solution().reverseList(l1))
