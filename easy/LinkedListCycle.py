'''
Given a linked list, determine if it has a cycle in it.
'''
import sys
sys.path.append("../datastuctures")
from linkedlist.linkedlist import ListNode
def checkCycle(head):
    '''
        Returns True if there is a cycle else returns False
    '''
    if not head:
        return False
    s,f = head,head.next
    while s and f:
        if s == f:
            return True
        s=s.next
        if f.next==None:
            return False
        f=f.next.next
    return False

l1 = ListNode(1)(ListNode(2))
l2 = None
l3 = ListNode(3)(ListNode(4)(ListNode(5)))
l3.appendRight(l3)

assert False == checkCycle(l1)
assert False == checkCycle(l2)
assert True == checkCycle(l3)
