# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if we dont have q and p then true
        # if we dont have q xor p then false
        # we nee to compare thevalues of p.rihgt and q.right etc.

        if not q and not p:
            return True

        if (p and q) and p.val == q.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(q.left, p.left)
        else:
            return False