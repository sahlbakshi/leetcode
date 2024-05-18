# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        def dfs(root, level):
            if root is None:
                return
            
            if level >= len(res):
                res.append([])
            res[level].append(root.val)
            level += 1
            left = dfs(root.left, level)
            right = dfs(root.right, level)
            return
        
        dfs(root, 0)
        return res
        