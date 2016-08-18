'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''

import sys
sys.path.append("../../datastuctures")
from tree.binarytree import TreeNode

class Solution:

    def binaryTreePaths(self, root):
        if not root:
            return []

        s = []
        s.append((root, []))
        result = []
        while s:
            n, path = s.pop()

            path.append(str(n.val))

            if not n.left and not n.right:
                result.append("->".join(path))
                continue
            if n.left:
                s.append((n.left, path[:]))
            if n.right:
                s.append((n.right, path[:]))
        return result

if __name__ == "__main__":
    t1 = TreeNode(1)(TreeNode(2)(TreeNode(5)), TreeNode(3))
    assert ["1->3", "1->2->5"] == Solution().binaryTreePaths(t1)