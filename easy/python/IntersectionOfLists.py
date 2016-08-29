"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""

import sys
sys.path.append("../../datastuctures")
from linkedlist.linkedlist import ListNode



class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        shorter = headA if lenA<=lenB else headB
        longer = headA if lenA>lenB else headB
        i = 0
        while abs(lenA-lenB) > i:
            longer = longer.next
            i+=1
        while longer and shorter:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next
        return None
    def getLength(self,head):
        length = 0
        current = head
        while current:
            current = current.next
            length+=1
        return length


if __name__ == "__main__":
    common = ListNode(1)(ListNode(3)(ListNode(7)))
    l1 = ListNode(5)(ListNode(99)(common))
    l2 = ListNode(5)(common)

    assert common == Solution().getIntersectionNode(l1,l2)
    assert None == Solution().getIntersectionNode(l1,None)