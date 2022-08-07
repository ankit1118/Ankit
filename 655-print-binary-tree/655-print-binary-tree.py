# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
		# 1. Find height of BT
        h = height(root) - 1
        
        rows = h + 1
        cols = pow(2, h + 1) -1
        # 2. Create  a res matrix and intialize with ""
        res = [["" for _ in range(cols)] for _ in range(rows)]
        
        def dfs(root, r , c):
            if not root:
                return
            
            res[r][c] = str(root.val)
            dfs(root.left, r + 1, c - pow(2, h - r - 1))
            dfs(root.right, r + 1, c + pow(2, h - r - 1))
            return
        # 3. Fill the matrix recursively
        dfs(root, 0, (cols - 1) // 2)
        return res