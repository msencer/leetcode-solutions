'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
'''
import sys
sys.path.append("../")
from data-stuctures.linkedlist.linkedlist import ListNode

class Solution(object):
        def deleteNode(self, node):
            if node.next == None: #tail node
                return
            node.val = node.next.val
            node.next = node.next.next

s = Solution()
midNode = ListNode(3)
sampleList = ListNode(1)(ListNode(2)(midNode(ListNode(4))))
s.deleteNode(mıdNode)
assert "1,2,4" == str(sampleList)
