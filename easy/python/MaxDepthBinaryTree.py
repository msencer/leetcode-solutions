'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
import sys
sys.path.append("../../datastuctures")
from tree.binarytree import TreeNode

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        return max(leftMax, rightMax) + 1

if __name__=="__main__":
    t1 = TreeNode(1)(TreeNode(2),TreeNode(3)(TreeNode(4),TreeNode(5)))
    t2 = TreeNode(1)
    assert 3 == Solution().maxDepth(t1)
    assert 1 == Solution().maxDepth(t2)
    assert 0 == Solution().maxDepth(None)