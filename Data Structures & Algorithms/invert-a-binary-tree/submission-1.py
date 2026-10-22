# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # can do recursion
        # a binary tree needs two children so we don't need to worry abouut the case hwere hteres 1

        if not root:
            return None
        
        root.right, root.left = root.left, root.right

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root