import sys
sys.path.append("../../datastuctures")
from linkedlist.linkedlist import ListNode

def mergeLists(l1,l2):
    d = ListNode(-1)
    head = d
    while l1 and l2:
        if l1.val > l2.val:
            d.next = l2
            l2 = l2.next
        else:
            d.next=l1
            l1=l1.next
        d = d.next
    if l1:
        d.next = l1
    elif l2:
        d.next = l2
    return head.next





l1 = ListNode(1)(ListNode(55)(ListNode(56)(ListNode(101))))
l2 = ListNode(-4)(ListNode(22)(ListNode(57)))
assert "-4,1,22,55,56,57,101" == str(mergeLists(l1,l2))
