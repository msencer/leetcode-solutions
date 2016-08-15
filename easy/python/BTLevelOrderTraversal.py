'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''
import sys
sys.path.append("../../datastuctures")
from tree.binarytree import TreeNode

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        result,current = [],[root]
        while current:
            nextLevel,vals = [],[]
            for n in current:
                vals.append(n.val)
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
            current = nextLevel
            result.append(vals)
        return result

if __name__ == "__main__":
    t1 = TreeNode(3)(TreeNode(9),TreeNode(20)(TreeNode(15),TreeNode(7)))
    assert [[3],[9,20],[15,7]]  == Solution().levelOrder(t1)