'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
'''
import sys
sys.path.append("../../datastuctures")
from tree.binarytree import TreeNode

class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not sum - root.val and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

if __name__ == "__main__":
    t1 = TreeNode(1)(TreeNode(2),TreeNode(3))
    t2 = TreeNode(1)(TreeNode(2))
    assert True == Solution().hasPathSum(t1,4)
    assert False == Solution().hasPathSum(t2, 1)