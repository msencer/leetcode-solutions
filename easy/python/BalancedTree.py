'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''
import sys
sys.path.append("../../datastuctures")
from tree.binarytree import TreeNode
class Solution(object):
    def getHeight(self, node):
        if not node:
            return 0
        h = 1
        maxHeight = 0
        s = [(node, h)]
        while s:
            n, ch = s.pop()
            if n.left:
                s.append((n.left, ch + 1))
            if n.right:
                s.append((n.right, ch + 1))
            maxHeight = max(ch, maxHeight)
        return maxHeight

    def isBalanced(self, root):
        if not root:
            return True

        s = [root]
        while s:
            n = s.pop()
            if abs(self.getHeight(n.left) - self.getHeight(n.right)) > 1:
                return False
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)

        return True

if __name__ == "__main__":
    t1 = TreeNode(1)(TreeNode(2)(TreeNode(3)))
    assert False == Solution().isBalanced(t1)