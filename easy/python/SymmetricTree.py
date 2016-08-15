'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''
import sys
sys.path.append("../../datastuctures")
from tree.binarytree import TreeNode
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        current = [root]
        while current:
            nextLevel = []
            for n in current:
                if not n:
                    continue
                nextLevel.append(n.left)
                nextLevel.append(n.right)
            i,j = 0,len(nextLevel)-1
            while i<=j:
                if (nextLevel[i] and nextLevel[j] and nextLevel[i].val!=nextLevel[j].val):
                    return False
                elif (nextLevel[i] and not nextLevel[j]) or (nextLevel[j] and not nextLevel[i]):
                    return False
                j-=1
                i+=1
            current = nextLevel
        return True

if __name__ == "__main__":
    t1 = TreeNode(1)(TreeNode(2)(TreeNode(3),TreeNode(4)),TreeNode(2)(TreeNode(4),TreeNode(3)))
    t2 = TreeNode(1)(TreeNode(2)(TreeNode(3),TreeNode(4)),TreeNode(2)(TreeNode(3),TreeNode(4)))

    assert True == Solution().isSymmetric(t1)
    assert False == Solution().isSymmetric(t2)