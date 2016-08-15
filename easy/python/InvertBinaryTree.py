'''
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

import sys
sys.path.append("../../datastuctures")
from tree.binarytree import TreeNode
from collections import deque

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = deque()
        if root:
            q.append(root)

        while (q):
            node = q.pop()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            temp = node.right
            node.right = node.left
            node.left = temp
        return root

if __name__ == "__main__":
    t1 = TreeNode(4)(TreeNode(2)(TreeNode(1),TreeNode(3)),TreeNode(7)(TreeNode(6),TreeNode(9)))
    assert [9,7,6,4,3,2,1] == Solution().invertTree(t1).inorder()
