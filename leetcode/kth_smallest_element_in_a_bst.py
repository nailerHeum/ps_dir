# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.k = 0
        
    def preorder(self, node):
        if node.left:
            is_here, val = self.preorder(node.left)
            if is_here:
                return (is_here, val)
        self.count += 1
        if self.count == self.k:
            return (True, node.val)
        if node.right:
            is_here, val = self.preorder(node.right)
            if is_here:
                return (is_here, val)
        return (False, 0)
            
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        _, val = self.preorder(root)
        return val
