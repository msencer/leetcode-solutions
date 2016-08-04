import sys
sys.path.append("../../datastuctures")
from tree.binarytree import TreeNode

def LCABinaryTree(root,p,q):
    if not root:
        return
    if root.val>p.val and root.val>q.val:
        return LCABinaryTree(root.left,p,q)
    elif root.val<p.val and root.val<q.val:
        return LCABinaryTree(root.right,p,q)
    else:
        return root

p =  TreeNode(2)(TreeNode(0),TreeNode(4)(TreeNode(3),TreeNode(5)))
q =  TreeNode(8)(TreeNode(7),TreeNode(9))
t1 = TreeNode(6)(p,q)
assert 6 == LCABinaryTree(t1,p,q).val
