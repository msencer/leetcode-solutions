'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

from collections import deque
import sys
sys.path.append("../../datastuctures")
from tree.binarytree import TreeNode


class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        q = deque([(root, 1)])
        while q:
            node, depth = q.pop()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.appendleft((node.left, depth + 1))
            if node.right:
                q.appendleft((node.right, depth + 1))

if __name__ == "__main__":
    t1 = TreeNode(1)(TreeNode(2), TreeNode(3)(TreeNode(4), TreeNode(5)))
    t2 = TreeNode(1)
    assert 2 == Solution().minDepth(t1)
    assert 1 == Solution().minDepth(t2)
    assert 0 == Solution().minDepth(None)
