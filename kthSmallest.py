# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        arr = self.getSortedArrayFromBST(root)
        return arr[k-1]

    def getSortedArrayFromBST(self, root):
        if root is None:
            return []
        
        return self.getSortedArrayFromBST(root.left) + [root.val] +  self.getSortedArrayFromBST(root.right)
        