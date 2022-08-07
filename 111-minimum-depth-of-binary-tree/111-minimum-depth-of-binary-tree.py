# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if (root == None):
            return 0
        self.height = 1<<30
        def depth(node,height):
            if (node):
                if (node.left == None) and (node.right == None):
                    self.height = min(self.height,height)
                if (node.left):
                    depth(node.left,height+1)
                if (node.right):
                    depth(node.right,height + 1)
        depth(root,1)
        return self.height
        