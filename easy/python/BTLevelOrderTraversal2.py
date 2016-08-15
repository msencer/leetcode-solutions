'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
'''
import sys
sys.path.append("../../datastuctures")
from tree.binarytree import TreeNode

class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []

        current = [root]
        result = []

        while current:
            nextLevel = []
            nValues = []
            for n in current:
                nValues.append(n.val)
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
            result.append(nValues)
            current = nextLevel
        return result[::-1]

if __name__== "__main__":
    t1 = TreeNode(1)(TreeNode(2)(TreeNode(4)),TreeNode(3))
    assert [[4],[2,3],[1]] == Solution().levelOrderBottom(t1)