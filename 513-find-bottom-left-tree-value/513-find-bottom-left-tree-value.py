# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        stack = [root]

        while stack:
            res = []
            temp = []
            for i in stack:
                if i:
                    if i.left:
                        temp.append(i.left)
                    if i.right:
                        temp.append(i.right)
                    res.append(i.val)
            stack = temp
                    
        return res[0]